FROM alpine:3.11 AS build

ARG CORSY_VERSION=1.0-beta

WORKDIR /opt/app

# Install Python and external dependencies, including headers and GCC
# RUN apk add --no-cache python3 python3-dev py3-pip libffi libffi-dev musl-dev gcc git ca-certificates openblas-dev musl-dev g++
RUN apk add --no-cache python3 python3-dev py3-pip git ca-certificates

# Install Pipenv
RUN pip3 install pipenv

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
	VIRTUAL_ENV="/opt/venv"

# Install dependencies into the virtual environment with Pipenv
RUN git clone --depth=1 -b ${CORSY_VERSION} https://github.com/s0md3v/Corsy /opt/app \
	&& cd /opt/app \
	&& pip3 install --upgrade pip \
	&& pip3 install -r requirements.txt

FROM alpine:3.11
MAINTAINER x0rxkov <x0rxkov@protonmail.com>

ARG VERSION=${VERSION:-"1.0-beta"}
ARG BUILD
ARG NOW

# Create runtime user
RUN mkdir -p /opt \
	&& adduser -D corsy -h /opt/app -s /bin/sh \
 	&& su corsy -c 'cd /opt/app; mkdir -p data'

# Install Python and external runtime dependencies only
RUN apk add --no-cache python3

# Switch to user context
USER corsy
WORKDIR /opt/corsy

# Copy the virtual environment from the previous image
COPY --chown=corsy:corsy --from=build /opt/venv /opt/venv
COPY --chown=corsy:corsy --from=build /opt/app /opt/corsy

# Activate the virtual environment
ENV PATH="/opt/venv/bin:/opt/corsy:$PATH" \
	VIRTUAL_ENV="/opt/venv" 

LABEL name="twint" \
      version="$VERSION" \
      build="$BUILD" \
      architecture="x86_64" \
      build_date="$NOW" \
      vendor="s0md3v" \
      maintainer="x0rzkov <x0rzkov@protonmail.com>" \
      url="https://github.com/s0md3v/Corsy" \
      summary="Dockerized CORS Misconfiguration Scanner" \
      description="Dockerized CORS Misconfiguration Scanner" \
      vcs-type="git" \
      vcs-url="https://github.com/s0md3v/Corsy" \
      vcs-ref="$VERSION" \
      distribution-scope="public"

RUN ls -l /opt/corsy && \
    chmod +x /opt/corsy/corsy.py

ENTRYPOINT ["/opt/corsy/corsy.py"]
