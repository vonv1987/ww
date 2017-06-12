#!/usr/bin/python
# -*- coding: UTF-8 -*-
from macpath import join

x = 9.234234
print "%5.3f" % 5, x, 9
print '-' * 40

pi = 3.1415926
print "%*.*f " % (10, 2, pi)
print '-' * 40

t = "32452213223333333"
print t.count("3")
print '-' * 40

text = "China    is in   developing."
words = text.split()  # 默认以“空白格”分开
print words

new_text = ' '.join(words)
print new_text

print 'new_text.lower() -->', new_text.lower()
print 'new_text.upper() -->', new_text.upper()
print 'new_text.title() -->', new_text.title()

from string import maketrans

table = maketrans("opqs", "sear")
# print table

text = "i love python"
secret_code = text.translate(table)
print "text ->", text
print "secret_code ->", secret_code
print "secret.translate(table)", secret_code.translate(table)

help(dict)
