#!/usr/bin/python

l = [6,8,1,5,2,4,3,7]

'''sorted does not alter the original list'''
sorted(l)
print l

l = sorted(l)
print l

l = sorted(l,reverse=True)
print l

'''
use the return value of function for sort
function should take one elem from the list and return one value
'''
l = ['one','elephant','three','four']
print sorted(l,key=len)

l = ['a','aa','b','bb','c','cc']

'''sort order: string starts with c, then a, then b'''
def mysort(s):
   if s[0] == 'c':
      return 0
   if s[0] == 'a':
      return 1
   elif s[0] == 'b':
      return 2

l = sorted(l,key=mysort)
print l
