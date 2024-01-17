import math

class Shape(object):

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return self.name


def describe_shape(shape):
    print('The area of a %s is %s.' % (shape.get_name(), shape.get_area()))
    print('The perimeter of a %s is %s.' % (shape.get_name(), shape.get_perimeter()))


# Your code below

class Triangle(Shape):
    pass
