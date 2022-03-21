#! /usr/bin/env python3

# $Id: test_get_parser_class.py 9011 2022-02-21 13:53:31Z milde $
# Author: grubert abadger1999
# Maintainer: docutils-develop@lists.sourceforge.net
# Copyright: This module has been placed in the public domain.

"""
test get_parser_class
"""

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport
from docutils.parsers import get_parser_class

class GetParserClassTestCase(DocutilsTestSupport.StandardTestCase):

    def test_registered_parser(self):
        rdr = get_parser_class('rst')
        # raises ImportError on failure

    def test_bogus_parser(self):
        with self.assertRaises(ImportError):
            get_parser_class('nope')

    def test_local_parser(self):
        # requires local-parser.py in test directory (testroot)
        wr = get_parser_class('local-parser')

if __name__ == '__main__':
    import unittest
    unittest.main()
