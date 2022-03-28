#! /usr/bin/env python3

# $Id: test_expose_internals.py 8925 2022-01-03 23:48:58Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This module has been placed in the public domain.

"""
Test module for universal.ExposeInternals transform.
"""

if __name__ == '__main__':
    import __init__
from test_transforms import DocutilsTestSupport # before importing docutils!
from docutils.transforms.universal import ExposeInternals
from docutils.parsers.rst import Parser


def suite():
    parser = Parser()
    s = DocutilsTestSupport.TransformTestSuite(
        parser, suite_settings={'expose_internals': ['rawsource', 'source']})
    s.generateTests(totest)
    return s


totest = {}

totest['transitions'] = ((ExposeInternals,), [
["""\
This is a test.
""",
"""\
<document internal:rawsource="" source="test data">
    <paragraph internal:rawsource="This is a test." internal:source="test data">
        This is a test.
"""],
])


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
