#! /usr/bin/env python3

# $Id: test_strip_elements_with_class.py 8993 2022-01-29 13:20:04Z milde $
# Author: Guenter Milde <milde@users.sf.net>
# Copyright: This module has been placed in the public domain.

"""
Tests for docutils.transforms.universal.StripClassesAndElements.
"""

if __name__ == '__main__':
    import __init__
from test_transforms import DocutilsTestSupport
from docutils.parsers.rst import Parser
from docutils.transforms.universal import StripClassesAndElements

def suite():
    parser = Parser()
    s = DocutilsTestSupport.TransformTestSuite(parser,
            suite_settings={'strip_elements_with_classes': ['spam', 'no-ham'],
                            'strip_classes': ['spam', 'noise']})
    s.generateTests(totest)
    return s

totest = {}

totest['strip_spam'] = ((StripClassesAndElements,), [
["""\
not classy

.. class:: spam

this is spam

.. class:: ham noise

this is ham

.. code::
   :class: spam
   \n\
   print("spam")
   \n\
.. image:: spam.jpg
   :class: spam

this is not ham
""",
"""\
<document source="test data">
    <paragraph>
        not classy
    <paragraph classes="ham">
        this is ham
    <paragraph>
        this is not ham
"""],
])


if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
