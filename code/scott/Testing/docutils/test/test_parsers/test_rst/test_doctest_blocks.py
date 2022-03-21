#! /usr/bin/env python3

# $Id: test_doctest_blocks.py 8925 2022-01-03 23:48:58Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for states.py.
"""

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport


def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['doctest_blocks'] = [
["""\
Paragraph.

>>> print("Doctest block.")
Doctest block.

Paragraph.
""",
"""\
<document source="test data">
    <paragraph>
        Paragraph.
    <doctest_block xml:space="preserve">
        >>> print("Doctest block.")
        Doctest block.
    <paragraph>
        Paragraph.
"""],
["""\
Paragraph.

>>> print("    Indented output.")
    Indented output.
""",
"""\
<document source="test data">
    <paragraph>
        Paragraph.
    <doctest_block xml:space="preserve">
        >>> print("    Indented output.")
            Indented output.
"""],
["""\
Paragraph.

    >>> print("    Indented block & output.")
        Indented block & output.
""",
"""\
<document source="test data">
    <paragraph>
        Paragraph.
    <block_quote>
        <doctest_block xml:space="preserve">
            >>> print("    Indented block & output.")
                Indented block & output.
"""],
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
