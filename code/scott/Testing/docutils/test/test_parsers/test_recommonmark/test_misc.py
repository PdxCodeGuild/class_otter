#!/usr/bin/env python3
# :Copyright: © 2020 Günter Milde.
# :License: Released under the terms of the `2-Clause BSD license`_, in short:
#
#    Copying and distribution of this file, with or without modification,
#    are permitted in any medium without royalty provided the copyright
#    notice and this notice are preserved.
#    This file is offered as-is, without any warranty.
#
# .. _2-Clause BSD license: https://opensource.org/licenses/BSD-2-Clause

"""
Various tests for the recommonmark parser.
"""

import unittest

if __name__ == '__main__':
    import __init__
from test_parsers import DocutilsTestSupport # must be imported before docutils
from docutils import core, utils, parsers
from docutils.core import publish_string

# Import `docutils.parsers.recommonmark_wrapper` and
# the optional `recommonmark.parser`. Create parser instance.
try:
    parser = parsers.get_parser_class('recommonmark')()
except ImportError:
    parser = None

sample_with_html = """\
A paragraph:

<p>A HTML block.</p>

Next paragraph.

<script type="text/javascript">
// some dangerous JavaScript

Final paragraph.
"""

@unittest.skipUnless(parser, 'Optional "recommonmark" module not found.')
class RecommonmarkParserTests(unittest.TestCase):

    def test_parser_name(self):
        # cf. ../test_rst/test_directives/test__init__.py
        # this is used in the "include" directive's :parser: option.
        self.assertEqual(parsers.rst.directives.parser_name('recommonmark'),
                         parsers.recommonmark_wrapper.Parser)

    def test_raw_disabled(self):
        output = publish_string(sample_with_html, parser=parser,
                                settings_overrides={'warning_stream': '',
                                                    'raw_enabled': False})
        self.assertNotIn(b'<raw>', output)
        self.assertIn(b'<system_message', output)
        self.assertIn(b'Raw content disabled.', output)

    def test_raw_disabled_inline(self):
        output = publish_string('foo <a href="uri">', parser=parser,
                                settings_overrides={'warning_stream': '',
                                                    'raw_enabled': False,
                                                   })
        self.assertNotIn(b'<raw>', output)
        self.assertIn(b'<system_message', output)
        self.assertIn(b'Raw content disabled.', output)


@unittest.skipIf(parser, 'Optional "recommonmark" module found.')
class RecommonmarkMissingTests(unittest.TestCase):

    def test_missing_parser_message(self):
        with self.assertRaisesRegex(ImportError,
                                    'requires the package .*recommonmark'):
            publish_string(sample_with_html, parser_name='recommonmark')


if __name__ == '__main__':
    unittest.main()
