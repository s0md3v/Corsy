
<h1 align="center">
  <br>
  <a href="https://github.com/s0md3v/Corsy"><img src="https://i.ibb.co/K0Z7X99/corsy.png" alt="Corsy"></a>
  <br>
  Corsy
  <br>
</h1>

<h4 align="center">CORS Misconfiguration Scanner</h4>

<p align="center">
  <a href="https://github.com/s0md3v/Corsy/releases">
    <img src="https://img.shields.io/github/release/s0md3v/Corsy.svg">
  </a>
  <a href="https://github.com/s0md3v/Corsy/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed-raw/s0md3v/Corsy.svg">
  </a>
</p>

### Introduction
Corsy is a lightweight program that scans for all known misconfigurations in CORS implementations.

![demo](https://i.ibb.co/478BCyb/corsy.png)

### Requirements
Corsy only works with `Python 3` and has the following depencies:

- `tld`
- `requests`

To install these dependencies, navigate to Corsy directory and execute `pip3 install -r requirements.txt`

### Usage
Using Corsy is pretty simple

`python3 corsy.py -u https://example.com`

A delay between consecutive requests can be specified with `-d` option.

If you're testing a site with an invalid SSL certificate, you can disable verification with `-k` option.

> *Note:* This is a beta version, features such as JSON output and scanning multiple hosts will be added later.

### Tests implemented
- Pre-domain bypass
- Post-domain bypass
- Backtick bypass
- Null origin bypass
- Unescaped dot bypass
- Invalid value
- Wild card value
- Origin reflection test
- Third party allowance test
- HTTP allowance test
### Support the developer
Liked the project? Donate a few bucks to motivate me to keep writing code for free.

[![Donate](https://i.ibb.co/1R5wK5S/28491754-14774f54-6f14-11e7-9975-8a5faeda7e30.gif)](https://s0md3v.github.io/donate.html)
