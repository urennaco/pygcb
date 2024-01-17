import unittest

from shapes import Triangle
from shapes import describe_shape

triangles = [
    [0, 0, 0],
    [1, 1, 1],
    [1, 2, 1],
    [5, 10, 12],
]

perimeters = [0, 3, 4, 27]
areas = [0, 0.4330127018922193, 0, 24.544602257930357]

def array_to_triangle(a):
    return Triangle(a[0], a[1], a[2])

class TestShapes(unittest.TestCase):

    def test_perimeter(self):
        for i in range(len(triangles)):
            my_triangle = array_to_triangle(triangles[i])
            self.assertEqual(my_triangle.get_perimeter(), perimeters[i])

    def test_area(self):
        for i in range(len(triangles)):
            my_triangle = array_to_triangle(triangles[i])
            self.assertEqual(my_triangle.get_area(), areas[i])
    
    def test_name(self):
        for a in triangles:
            my_triangle = array_to_triangle(a)
            self.assertEqual(my_triangle.get_name(), 'Triangle')

if __name__ == '__main__':
    unittest.main()
