#!/usr/bin/python

'''
Attribute references use the standard syntax used for all attribute references in Python: obj.name. Valid attribute names are all the names that were in the class’s namespace when the class object was created.

    class MyClass:
        """A simple example class"""
        i = 12345

        def f(self):
            return 'hello world'

Note that x.f() is the same as MyClass.f(x)

__doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".

Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class.

    x = MyClass()

The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__().

    def __init__(self):
        self.data = []
'''

# Two Simple Example Classes #

# -----------------------------------------
class Point:

    # class variable
    numpnts = 0

    # constructor
    def __init__(self, x, y):
        # instance variables
        self.x = x
        self.y = y

    # class method
    def getpnt(self):
        print('Point at location: ' + str(self.x) + ' ' + str(self.y))
# -----------------------------------------
print('=== Point Class ===\n')

# initialize point object
p = Point(3,4)

# call its methods
p.getpnt()

# access and change class variable
Point.numpnts += 1
print('Class variable after increment: ' + str(p.numpnts))

# class variable retains value even with new object
p2 = Point(5,6)
Point.numpnts += 1
print('Class variable for new object: ' + str(p2.numpnts))


# ------------------------------------------
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
# ------------------------------------------
print('\n=== Shape Class ===\n')

rectangle = Shape(100, 45)

#describing the rectangle
rectangle.describe("A wide rectangle, more than twice\
 as wide as it is tall")
print('Description: {}'.format(rectangle.description))

#finding the area of your rectangle:
print('Area: {}'.format(rectangle.area()))

#finding the perimeter of your rectangle:
print('Perimeter: {}'.format(rectangle.perimeter()))

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)

#re-printing the new area of the rectangle
print('New area after scaling: {}'.format(rectangle.area()))

# --------- Inheritance ----------
'''
class DerivedClassName(BaseClassName):
    * some attributes and methods *

Specify the parent class when defining a child class.

For C++ programmers: All methods in Python are effectively virtual.
'''

class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x

# ------ Multiple Inheritance ------
'''
class DerivedClassName(Base1, Base2, Base3):
    * some attributes and methods *

For most purposes, in the simplest cases, you can think of the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. Thus, if an attribute is not found in DerivedClassName, it is searched for in Base1, then (recursively) in the base classes of Base1, and if it was not found there, it was searched for in Base2, and so on.
'''

# ------- Private Instance Variables and Name Mangling ------
'''
Declare private instance variable with double underscore:

class SomeClass():
    __init__(self,x):
        self.__myprivatevar = x

“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member).

Any identifier of the form __spam is textually replaced with classname__spam.
'''

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# -------- Structs in Python ---------
'''
Use an empty class definition
'''

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
