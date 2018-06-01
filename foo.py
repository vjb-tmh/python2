#!/usr/bin/python

#v = raw_input()
#print v

d = {'a':1,'b':2}
for k in sorted(d.keys()):
   print str(k) + ' ' + str(d[k])

for k,v in d.items():
   print str(k) + ' ' + str(v)

f = open('file.txt','rU')
for line in f:
   l = line.strip().split(' ')
   d[l[0]] = l[1]

for k,v in d.items():
   print str(k) + ' ' + str(v)

for k in d.keys():
   d[k] = 0
   print d[k]

s = 'always bring a towel and don\'t panic'

s = s.replace('towel','banana')
i = s.find('banana')
s = s[:i] + 'ripe ' + s[i:]
print s

l = [1,2,3,4,5]
l.append(77)
l.remove(3)
l.pop(l.index(2))
l.insert(l.index(4),999)
print l

class fooclass:
   name = ''
   myint = 0

   def __init__(self,name,myint):
      self.name = name
      self.myint = myint

   def printclass(self):
      print self.name + ' ' + str(self.myint)

f = fooclass('baz',77)
f.printclass()

