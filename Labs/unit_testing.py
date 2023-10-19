import unittest
import math
from Lab3 import Circle, Rectangle, Cube, Sphere

class TestShapes(unittest.TestCase):
    # Circle testing
    def test_circle(self):
        circle = Circle(x=0, y=0, radius=1)
        self.assertAlmostEqual(circle.area, math.pi)

    def test_circle_is_inside(self):
        circle = Circle(x=0, y=0, radius=1)
        self.assertTrue(circle.is_inside(0.5, 0.5))

    # Rectangle testing
    def test_rectangle(self):
        rectangle = Rectangle(x=0, y=0, side1=2, side2=3)
        self.assertAlmostEqual(rectangle.area, 6)

    def test_rectangle_is_inside(self):
        rectangle = Rectangle(x=0, y=0, side1=2, side2=3)
        self.assertTrue(rectangle.is_inside(0, 0))
        self.assertTrue(rectangle.is_inside(1, 1))
        self.assertTrue(rectangle.is_inside(-1, -1))

    # Cube testing
    def test_cube(self):
        cube_instance = Cube(x=0, y=0, z=0, side_length=6)
        expected_volume = 6 ** 3
        self.assertEqual(cube_instance.volume(), expected_volume)

    def test_cube_is_inside(self):
        cube_instance = Cube(x=0, y=0, z=0, side_length=6)
        self.assertTrue(cube_instance.is_inside(0, 0, 0))
        self.assertTrue(cube_instance.is_inside(3, 3, 3))
        self.assertTrue(cube_instance.is_inside(-3, -3, -3))

        self.assertFalse(cube_instance.is_inside(8, 0, 0))
        self.assertFalse(cube_instance.is_inside(0, 8, 0))
        self.assertFalse(cube_instance.is_inside(0, 0, 8))


    # sphere testing
    def test_sphere_surface_area(self):
        sphere_instance = Sphere(x=0, y=0, z=0, radius=5)
        expected_surface_area = 4 * math.pi * 5 ** 2
        self.assertEqual(sphere_instance.surface_area(), expected_surface_area)

    def test_sphere_volume(self):
        sphere_instance = Sphere(x=0, y=0, z=0, radius=5)

        expected_volume = (4 / 3) * math.pi * 5 ** 3
        self.assertAlmostEqual(sphere_instance.volume, expected_volume)

    def test_sphere_is_inside(self):
        sphere_instance = Sphere(x=0, y=0, z=0, radius=5)
        self.assertTrue(sphere_instance.is_inside(1, 1, 1))
        self.assertTrue(sphere_instance.is_inside(0, 0, 5))
     



if __name__ == '__main__':
    unittest.main()

