#!/usr/bin/python

'''
newlist = [ expr for item in list]
   expr is applied to each item in list
   expr can be a function
'''

#------------------------------------------
nums = [1,2,3,4,5]
squares = [n*n for n in nums]
print squares
#------------------------------------------

#------------------------------------------
'''
Use functions as the expr
'''
def tripler(n):
   return n * 3

triples = [tripler(s) for s in nums]
print triples
#------------------------------------------

#------------------------------------------
'''
Use built-ins
'''
slist = ['foo','bar','baz']
slist = [s.upper() + '!' for s in slist]
print slist
#------------------------------------------

#------------------------------------------
'''
Apply conditions and conversions
'''
nums = [33,2,10,7,9,1,777]
small_num_strings = [str(n) for n in nums if n < 10]
print small_num_strings

fruits = ['apple','kiwi','orange','banana','lemon']
nona_fruits = [s for s in fruits if 'a' not in s]
print nona_fruits
nonae_fruits = [s for s in fruits if 'a' not in s and 'e' in s]
print nonae_fruits
#------------------------------------------
