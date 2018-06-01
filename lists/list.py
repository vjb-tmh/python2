#!/usr/bin/python
'''
append(elem)
insert(index, elem)
remove(elem)
pop(index)
index(elem)
in / not in
list1 + list2, list1.extend(list2)
sort()
reverse()
for thing in list
list1[0:2] = ['a','b'] # replace 1st and 2nd elem with new elems

list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.

list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.

list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().

list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).

list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)

list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)

list.reverse() -- reverses the list in place (does not return it)

list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
'''

import sys

'''
BASICS
'''

l = ['red','green','blue']
print l
print len(l)

# note that list assignment assigns a pointer to the list memory
def change_list(l):
   l[0] = 'purple'

a = l
change_list(a)
print l

print 'Colors in the list: '
for color in l:
   sys.stdout.write(str(color) + ' ')
print

if 'blue' in l:
   print 'blue in list'

l = ['larry', 'curly', 'moe']
l.append('shemp')          ## append elem at end
print l
l.insert(0, 'xxx')         ## insert elem at index 0
print l
l.extend(['yyy', 'zzz'])   ## add list of elems at end,
                           ## almost identical to +
print l
print l.index('curly')     ## 2

l.remove('curly')          ## search and remove that element
l.pop(1)                   ## removes and returns 'larry'
print l                    ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

l[0:2] = ['foo','bar']     # change first two elems
print l

'''
USEFUL COMBOS
'''
l = ['red', 'blue', 'green', 'purple', 'yellow']

# get index and insert in front
l.insert(l.index('green'),'FOO')
# get index and insert behind
l.insert(l.index('green') + 1,'BAR')

print l

# pop from one list and append in another
a = [1,2,3,4,5]
a.append(l.pop(2))

print a
print

def f(s):
   print 'Function in list prints: ' + s

l = ['foobar',f]
l[1]('wombat')

def f2(s):
   print 'New function prints: ' + s

l[1] = f2
l[1]('dragon')
