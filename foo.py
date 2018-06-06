#!/usr/bin/python

def vinsert(s,fword,iword):
    i = s.find(fword)
    return (s[:i] + iword + ' ' + s[i:])

mystr = 'one two three'
mystr = vinsert(mystr,'two','seven')
print(mystr)

def greet(*names):
    for name in names:
        print(name)

greet('peter','paul')

def fact(i):
    if i == 0:
        return 1
    return i * fact(i - 1)

print(fact(4))

m = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        m[i][j] = 7

l = [' foo ','bar   ', '  baz ']
l = [s.strip() for s in l]
print(l)

l = []
f = open('myfile','rU')
for line in f:
    l.append(line.strip().split())

