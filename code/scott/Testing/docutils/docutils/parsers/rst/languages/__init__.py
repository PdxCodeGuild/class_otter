# $Id: __init__.py 8979 2022-01-26 19:05:07Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

# Internationalization details are documented in
# <https://docutils.sourceforge.io/docs/howto/i18n.html>.

"""
This package contains modules for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'


from docutils.languages import LanguageImporter

class RstLanguageImporter(LanguageImporter):
    """Import language modules.

    When called with a BCP 47 language tag, instances return a module
    with localisations for "directive" and "role" names for  from
    `docutils.parsers.rst.languages` or the PYTHONPATH.

    If there is no matching module, warn (if a `reporter` is passed)
    and return None.
    """
    packages = ('docutils.parsers.rst.languages.', '')
    warn_msg = 'rST localisation for language "%s" not found.'
    fallback = None

    def check_content(self, module):
        """Check if we got an rST language module."""
        if not (isinstance(module.directives, dict)
                and isinstance(module.roles, dict)):
            raise ImportError

get_language = RstLanguageImporter()