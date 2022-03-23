#! /usr/bin/env python3

# $Id: test_title.py 8925 2022-01-03 23:48:58Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Tests for the 'title' directive.
"""

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['title'] = [
["""\
.. title:: This is the document title.
""",
"""\
<document source="test data" title="This is the document title.">
"""],
]


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
