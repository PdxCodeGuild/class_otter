#!/usr/bin/env python3

# $Id: test_null.py 8925 2022-01-03 23:48:58Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Test for Null writer.
"""

if __name__ == '__main__':
    import __init__
from test_writers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.PublishTestSuite('null')
    s.generateTests(totest)
    return s

totest = {}

totest['basic'] = [
["""\
This is a paragraph.
""",
None]
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
