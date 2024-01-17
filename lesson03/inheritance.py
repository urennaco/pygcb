
class Shape(object):

    def __init__(self, name):
        self.name = name

    def get_area(self):
        return None

    def get_perimeter(self):
        return None

    def get_name(self):
        return self.name


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__('Rectangle')
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.name = 'Square'


def describe_shape(shape):
    print('The area of the %s is %s.' % (shape.get_name(), shape.get_area()))
    print('The perimeter of the %s is %s.' % (shape.get_name(), shape.get_perimeter()))


s = Square(8)
describe_shape(s)
