#! /usr/bin/env python3

# $Id: test_get_reader_class.py 9011 2022-02-21 13:53:31Z milde $
# Author: grubert abadger1999
# Maintainer: docutils-develop@lists.sourceforge.net
# Copyright: This module has been placed in the public domain.

"""
test get_reader_class
"""

if __name__ == '__main__':
    import __init__
from test_readers import DocutilsTestSupport
from docutils.readers import get_reader_class


class GetReaderClassTestCase(DocutilsTestSupport.StandardTestCase):

    def test_registered_reader(self):
        rdr = get_reader_class('pep')
        # raises ImportError on failure

    def test_bogus_reader(self):
        with self.assertRaises(ImportError):
            get_reader_class('nope')

    def test_local_reader(self):
        # requires local-reader.py in test directory (testroot)
        wr = get_reader_class('local-reader')

if __name__ == '__main__':
    import unittest
    unittest.main()
