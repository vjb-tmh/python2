#!/usr/bin/python

'''
len()
count()
find()
split()
splitlines()
join()
replace()
startswith()
endswith()
[#:#]
string * #
''.join(reversed(str))
strip()
lstrip()
rstrip()
str1 + str2
upper()
lower()
swapcase()

word.isalnum()         #check if all char are alphanumeric
word.isalpha()         #check if all char in the string are alphabetic
word.isdigit()         #test if string contains digits
word.istitle()         #test if string contains title words
word.isupper()         #test if string contains upper case
word.islower()         #test if string contains lower case
word.isspace()         #test if string contains spaces
word.endswith('d')     #test if string endswith a d
word.startswith('H')   #test if string startswith H
'''

mystr = 'gamma particles'
print(mystr[0])

# len
print(len(mystr))

# count
print(mystr.count('m'))

# find, returns -1 on not found
print(mystr.find('part'))

# slicing
print(mystr[0:5])
print(mystr[6:])
print(mystr[:-3])
print(mystr[mystr.find('p'):mystr.find('i')])

# split
mystr = '1|2|3|4|5'
newstr = mystr.split('|')
print(newstr)

s = '''always bring a towel
and don't panic'''
print(s.splitlines())

# join
l = ['first line','second line']
print('\n'.join(l))
print('******'.join(l))

# startswith, endswith
print(mystr.startswith('1'))
print(mystr.endswith('5'))

# repeat
mystr = '7'*6
print(mystr)

# reverse
mystr = 'foobar'
print(''.join(reversed(mystr)))

# strip
mystr = '  foobar  '
print(mystr.strip())
print(mystr.lstrip())
print(mystr.rstrip())

# strip specific char
s = '0000000WOMBAT000000'
print(s.strip('0'))

# replace
mystr = 'foobar'
print(mystr.replace('foo','xxx'))

# upper/lower
s = 'FoObAr'
print(s.upper())
print(s.lower())
print(s.swapcase())

s = 'foo bar baz'
print(s.title())

# center, ljust, rjust
s = 'foobar'
print(s.center(30))
print(s.ljust(30))
print(s.rjust(30))

print(s.rjust(30,'*'))

# formatted output
print('My formatted output: {0} {1}'.format(66,77))
print('My formatted output: {1} {0}'.format(66,77))
print('My formatted output: {first} {last}'.format(last=11,first=22))
print('My formatted output: {0:.2f}'.format(55.342342))


print('My formatted output: %d %s %.2f' % (88,'foobar',2.78576))

l = [99,'baz',4.3423]
print('My formatted output: %d %s %.2f' % tuple(l))

# insert a string into a string
s = 'always bring a towel and don\'t panic'

s = s.replace('towel','banana')
i = s.find('banana')
s = s[:i] + 'ripe ' + s[i:]
print(s)
