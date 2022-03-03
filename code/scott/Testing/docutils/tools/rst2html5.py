#!/usr/bin/env python3
# :Copyright: © 2015 Günter Milde.
# :License: Released under the terms of the `2-Clause BSD license`_, in short:
#
#    Copying and distribution of this file, with or without modification,
#    are permitted in any medium without royalty provided the copyright
#    notice and this notice are preserved.
#    This file is offered as-is, without any warranty.
#
# .. _2-Clause BSD license: https://opensource.org/licenses/BSD-2-Clause
#
# Revision: $Revision: 8983 $
# Date: $Date: 2022-01-26 22:09:36 +0000 (Wed, 26 Jan 2022) $

"""
A minimal front end to the Docutils Publisher, producing HTML 5 documents.

The output is also valid XML.
"""

try:
    import locale # module missing in Jython
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    pass

from docutils.core import publish_cmdline, default_description

description = ('Generates HTML5 documents from standalone '
               'reStructuredText sources.\n'
               + default_description)

publish_cmdline(writer_name='html5', description=description)
