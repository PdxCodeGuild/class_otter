#!/usr/bin/env python3
# :Id: $Id: punctuation_chars.py 8979 2022-01-26 19:05:07Z milde $
# :Copyright: © 2011, 2017 Günter Milde.
# :License: Released under the terms of the `2-Clause BSD license`_, in short:
#
#    Copying and distribution of this file, with or without modification,
#    are permitted in any medium without royalty provided the copyright
#    notice and this notice are preserved.
#    This file is offered as-is, without any warranty.
#
# .. _2-Clause BSD license: https://opensource.org/licenses/BSD-2-Clause
#
# This file is generated by
# ``docutils/tools/dev/generate_punctuation_chars.py``.
# ::

import sys
import unicodedata

"""Docutils character category patterns.

   Patterns for the implementation of the `inline markup recognition rules`_
   in the reStructuredText parser `docutils.parsers.rst.states.py` based
   on Unicode character categories.
   The patterns are used inside ``[ ]`` in regular expressions.

   Rule (5) requires determination of matching open/close pairs. However, the
   pairing of open/close quotes is ambiguous due to  different typographic
   conventions in different languages. The ``quote_pairs`` function tests
   whether two characters form an open/close pair.

   The patterns are generated by
   ``docutils/tools/dev/generate_punctuation_chars.py`` to  prevent dependence
   on the Python version and avoid the time-consuming generation with every
   Docutils run. See there for motives and implementation details.

   The category of some characters changed with the development of the
   Unicode standard. The current lists are generated with the help of the
   "unicodedata" module of Python 2.7.13 (based on Unicode version 5.2.0).

   .. _inline markup recognition rules:
      https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#inline-markup-recognition-rules
"""

openers = (u'"\'(<\\[{\u0f3a\u0f3c\u169b\u2045\u207d\u208d\u2329\u2768'
           u'\u276a\u276c\u276e\u2770\u2772\u2774\u27c5\u27e6\u27e8\u27ea'
           u'\u27ec\u27ee\u2983\u2985\u2987\u2989\u298b\u298d\u298f\u2991'
           u'\u2993\u2995\u2997\u29d8\u29da\u29fc\u2e22\u2e24\u2e26\u2e28'
           u'\u3008\u300a\u300c\u300e\u3010\u3014\u3016\u3018\u301a\u301d'
           u'\u301d\ufd3e\ufe17\ufe35\ufe37\ufe39\ufe3b\ufe3d\ufe3f\ufe41'
           u'\ufe43\ufe47\ufe59\ufe5b\ufe5d\uff08\uff3b\uff5b\uff5f\uff62'
           u'\xab\u2018\u201c\u2039\u2e02\u2e04\u2e09\u2e0c\u2e1c\u2e20'
           u'\u201a\u201e\xbb\u2019\u201d\u203a\u2e03\u2e05\u2e0a\u2e0d'
           u'\u2e1d\u2e21\u201b\u201f')
closers = (u'"\')>\\]}\u0f3b\u0f3d\u169c\u2046\u207e\u208e\u232a\u2769'
           u'\u276b\u276d\u276f\u2771\u2773\u2775\u27c6\u27e7\u27e9\u27eb'
           u'\u27ed\u27ef\u2984\u2986\u2988\u298a\u298c\u298e\u2990\u2992'
           u'\u2994\u2996\u2998\u29d9\u29db\u29fd\u2e23\u2e25\u2e27\u2e29'
           u'\u3009\u300b\u300d\u300f\u3011\u3015\u3017\u3019\u301b\u301e'
           u'\u301f\ufd3f\ufe18\ufe36\ufe38\ufe3a\ufe3c\ufe3e\ufe40\ufe42'
           u'\ufe44\ufe48\ufe5a\ufe5c\ufe5e\uff09\uff3d\uff5d\uff60\uff63'
           u'\xbb\u2019\u201d\u203a\u2e03\u2e05\u2e0a\u2e0d\u2e1d\u2e21'
           u'\u201b\u201f\xab\u2018\u201c\u2039\u2e02\u2e04\u2e09\u2e0c'
           u'\u2e1c\u2e20\u201a\u201e')
delimiters = (u'\\-/:\u058a\xa1\xb7\xbf\u037e\u0387\u055a-\u055f\u0589'
              u'\u05be\u05c0\u05c3\u05c6\u05f3\u05f4\u0609\u060a\u060c'
              u'\u060d\u061b\u061e\u061f\u066a-\u066d\u06d4\u0700-\u070d'
              u'\u07f7-\u07f9\u0830-\u083e\u0964\u0965\u0970\u0df4\u0e4f'
              u'\u0e5a\u0e5b\u0f04-\u0f12\u0f85\u0fd0-\u0fd4\u104a-\u104f'
              u'\u10fb\u1361-\u1368\u1400\u166d\u166e\u16eb-\u16ed\u1735'
              u'\u1736\u17d4-\u17d6\u17d8-\u17da\u1800-\u180a\u1944\u1945'
              u'\u19de\u19df\u1a1e\u1a1f\u1aa0-\u1aa6\u1aa8-\u1aad\u1b5a-'
              u'\u1b60\u1c3b-\u1c3f\u1c7e\u1c7f\u1cd3\u2010-\u2017\u2020-'
              u'\u2027\u2030-\u2038\u203b-\u203e\u2041-\u2043\u2047-'
              u'\u2051\u2053\u2055-\u205e\u2cf9-\u2cfc\u2cfe\u2cff\u2e00'
              u'\u2e01\u2e06-\u2e08\u2e0b\u2e0e-\u2e1b\u2e1e\u2e1f\u2e2a-'
              u'\u2e2e\u2e30\u2e31\u3001-\u3003\u301c\u3030\u303d\u30a0'
              u'\u30fb\ua4fe\ua4ff\ua60d-\ua60f\ua673\ua67e\ua6f2-\ua6f7'
              u'\ua874-\ua877\ua8ce\ua8cf\ua8f8-\ua8fa\ua92e\ua92f\ua95f'
              u'\ua9c1-\ua9cd\ua9de\ua9df\uaa5c-\uaa5f\uaade\uaadf\uabeb'
              u'\ufe10-\ufe16\ufe19\ufe30-\ufe32\ufe45\ufe46\ufe49-\ufe4c'
              u'\ufe50-\ufe52\ufe54-\ufe58\ufe5f-\ufe61\ufe63\ufe68\ufe6a'
              u'\ufe6b\uff01-\uff03\uff05-\uff07\uff0a\uff0c-\uff0f\uff1a'
              u'\uff1b\uff1f\uff20\uff3c\uff61\uff64\uff65')
if sys.maxunicode >= 0x10FFFF: # "wide" build
    delimiters += (u'\U00010100\U00010101\U0001039f\U000103d0\U00010857'
                   u'\U0001091f\U0001093f\U00010a50-\U00010a58\U00010a7f'
                   u'\U00010b39-\U00010b3f\U000110bb\U000110bc\U000110be-'
                   u'\U000110c1\U00012470-\U00012473')
closing_delimiters = u'\\\\.,;!?'


# Matching open/close quotes
# --------------------------

quote_pairs = {# open char: matching closing characters # usage example
               u'\xbb':   u'\xbb',         # » » Swedish
               u'\u2018': u'\u201a',       # ‘ ‚ Albanian/Greek/Turkish
               u'\u2019': u'\u2019',       # ’ ’ Swedish
               u'\u201a': u'\u2018\u2019', # ‚ ‘ German ‚ ’ Polish
               u'\u201c': u'\u201e',       # “ „ Albanian/Greek/Turkish
               u'\u201e': u'\u201c\u201d', # „ “ German „ ” Polish
               u'\u201d': u'\u201d',       # ” ” Swedish
               u'\u203a': u'\u203a',       # › › Swedish
              }
"""Additional open/close quote pairs."""

def match_chars(c1, c2):
    """Test whether `c1` and `c2` are a matching open/close character pair.

    Matching open/close pairs are at the same position in
    `punctuation_chars.openers` and `punctuation_chars.closers`.
    The pairing of open/close quotes is ambiguous due to  different
    typographic conventions in different languages,
    so we test for additional matches stored in `quote_pairs`.
    """
    try:
        i = openers.index(c1)
    except ValueError:  # c1 not in openers
        return False
    return c2 == closers[i] or c2 in quote_pairs.get(c1, u'')
