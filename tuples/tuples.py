#!/usr/bin/python

t = (1,2.7,'foo')
print t
print len(t)
print t[1]

t = (3,4.6,'bar')
# t[0] = 9  will throw an error. Tuples are immutable.

'''
Tuple of size 1
'''
t = ('foobar',) # the comma is necessary!

'''
Note that you can assign a tuple of variables using a tuple.
Sometimes functions return tuples for multiple assignment.
'''
(a,b,c) = (3.14,'baz',77)
print str(a) + ' ' + b + ' ' + str(c)

'''
Tuples behave kind of like immutable structs.
'''
def f(s):
   print s

t = ('foobar',f)
print t
t[1]('baz')
t[1](t[0])
