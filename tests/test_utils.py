import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.utils import normalize_url


class NormalizeUrlTest(unittest.TestCase):
    def test_preserves_query_string(self):
        url = 'https://example.com/search?q=xss&page=2'
        self.assertEqual(normalize_url(url), url)

    def test_preserves_path_parameters_and_fragment(self):
        url = 'https://example.com/items;v=1/list?sort=asc#results'
        self.assertEqual(normalize_url(url), url)

    def test_plain_url_is_unchanged(self):
        url = 'http://example.com/path'
        self.assertEqual(normalize_url(url), url)


if __name__ == '__main__':
    unittest.main()
