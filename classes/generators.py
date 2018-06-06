#!/usr/bin/python

'''
Generator functions return items, one by one, rather than an iterable.

Instead of 'return', they use the 'yield' built-in.

This can save memory, since an entire list, dict, etc. doesn't have to be built in memory.

Generators are a simple and powerful tool for creating iterators.

They are written like regular functions but use the yield statement whenever they want to return data.

Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).
'''

# --------------------------------------------
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
# --------------------------------------------


'''
Example of when a generator function is a good idea
'''
# --------------------------------------------
# Build and return a list
# But what if each number is 1MB or larger?
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(100000))
# --------------------------------------------

# --------------------------------------------
# Save memory by using a generator that
# yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Here, firstn() generator returns each item
# using consecutive calls to __next__()
sum_of_first_n = sum(firstn(100000))
# --------------------------------------------


'''
Generator Expressions vs List Comprehension

Generator expressions provide an additional shortcut to build generators out of expressions similar to that of list comprehensions.

We can turn a list comprehension into a generator expression by replacing the square brackets ("[ ]") with parentheses.

Alternately, we can think of list comprehensions as generator expressions wrapped in a list constructor.
'''

# list comprehension
doubles = [2 * n for n in range(50)]

# same as the list comprehension above
doubles = list(2 * n for n in range(50))


'''
Performance

There are many cases when using a generator is better than using an iterable.

Both range and xrange represent a range of numbers, and have the same function signature, but range returns a list while xrange returns a generator.
'''

# using a non-generator
sum_of_first_n = sum(range(1000000))

# using a generator
sum_of_first_n = sum(xrange(1000000))


