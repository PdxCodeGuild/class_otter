#! /usr/bin/env python3

# $Id: test_filter.py 8925 2022-01-03 23:48:58Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for docutils.transforms.components.Filter.
"""

if __name__ == '__main__':
    import __init__
from test_transforms import DocutilsTestSupport
from docutils.parsers.rst import Parser


def suite():
    parser = Parser()
    s = DocutilsTestSupport.TransformTestSuite(parser)
    s.generateTests(totest)
    return s

totest = {}

totest['meta'] = ((), [
["""\
.. meta::
   :description: The reStructuredText plaintext markup language
   :keywords: plaintext,markup language
""",
"""\
<document source="test data">
    <meta content="The reStructuredText plaintext markup language" name="description">
    <meta content="plaintext,markup language" name="keywords">
"""],
])


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
