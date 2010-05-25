#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import htmlentitydefs


def unescape(text):
   """Removes HTML or XML character references 
      and entities from a text string.
   @param text The HTML (or XML) source text.
   @return The plain text, as a Unicode string, if necessary.
   from Fredrik Lundh
   2008-01-03: input only unicode characters string.
   http://effbot.org/zone/re-sub.htm#unescape-html
   """
   def fixup(m):
      text = m.group(0)
      if text[:2] == "&#":
         # character reference
         try:
            if text[:3] == "&#x":
               return unichr(int(text[3:-1], 16))
            else:
               return unichr(int(text[2:-1]))
         except ValueError:
            print "Value Error"
            pass
      else:
         # named entity
         # reescape the reserved characters.
         try:
            if text[1:-1] == "amp":
               text = "&amp;amp;"
            elif text[1:-1] == "gt":
               text = "&amp;gt;"
            elif text[1:-1] == "lt":
               text = "&amp;lt;"
            else:
               print text[1:-1]
               text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
         except KeyError:
            print "keyerror"
            pass
      return text # leave as is
   return re.sub("&#?\w+;", fixup, text)

def main():

    file1 = open(sys.argv[1],'r')
    file2 = open(sys.argv[1][:-3]+'_h'+'.mm','w')

    buf_xml = file1.readlines()
    buf_str = buf_xml

    for i in range( len(buf_xml) ):
        buf_str[i] = unescape(buf_xml[i]).encode('utf8')

    file2.writelines(buf_str)

if __name__ == '__main__':
    main()