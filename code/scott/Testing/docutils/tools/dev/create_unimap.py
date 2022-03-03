#!/usr/bin/env python3

# $Id: create_unimap.py 8984 2022-01-26 22:10:06Z milde $
# Author: Lea Wiemann <LeWiemann@gmail.com>
# Copyright: This file has been placed in the public domain.

# Call: create_unimap.py < unicode.xml > unicode_latex.py
#
# Get unicode.xml from
# <https://www.w3.org/2003/entities/xml/unicode.xml>.

from xml.dom import minidom
import sys
import pprint


text_map = {}
math_map = {}


class Visitor:
    """Node visitor for contents of unicode.xml."""

    def visit_character(self, node):
        for n in node.childNodes:
            if n.nodeName == 'latex':
                code = node.attributes['dec'].value
                if '-' in code:
                    # I don't know what this means, but we probably
                    # don't need it....
                    continue
                if int(code) < 128:
                    # Wrong (maps "-" to "$-$", which is too wide) and
                    # unnecessary (maps "a" to "{a}").
                    continue
                latex_code = n.childNodes[0].nodeValue.encode('ascii').strip()
                if node.attributes['mode'].value == 'math':
                    math_map[chr(int(code))] = '$%s$' % latex_code
                else:
                    text_map[chr(int(code))] = '{%s}' % latex_code

def call_visitor(node, visitor=Visitor()):
    if isinstance(node, minidom.Text):
        name = 'Text'
    else:
        name = node.nodeName.replace('#', '_')
    if hasattr(visitor, 'visit_' + name):
        getattr(visitor, 'visit_' + name)(node)
    for child in node.childNodes:
        call_visitor(child)
    if hasattr(visitor, 'depart_' + name):
        getattr(visitor, 'depart_' + name)(node)

document = minidom.parse(sys.stdin)
call_visitor(document)

unicode_map = math_map
unicode_map.update(text_map)
# Now unicode_map contains the text entries plus dollar-enclosed math
# entries for those chars for which no text entry exists.

print('# $%s$' % 'Id')
print('# Author: Lea Wiemann <LeWiemann@gmail.com>')
print('# Copyright: This file has been placed in the public domain.')
print('')
print('# This is a mapping of Unicode characters to LaTeX equivalents.')
print('# The information has been extracted from')
print('# <https://www.w3.org/2003/entities/xml/unicode.xml>, written by')
print('# David Carlisle and Sebastian Rahtz.')
print('#')
print('# The extraction has been done by the "create_unimap.py" script')
print('# located at <https://docutils.sourceforge.io/tools/dev/create_unimap.py>.')
print('')
print('unicode_map = %s' % pprint.pformat(unicode_map, indent=0))
