import unittest
import math

def area_circle(r):
    return math.pi * r * r

def perimeter_circle(r):
    return 2 * math.pi * r

def area_square(a):
    return a * a

def perimeter_square(a):
    return 4 * a

class TestGeometryFunctions(unittest.TestCase):
    
    def test_area_circle(self):
        self.assertAlmostEqual(area_circle(1), math.pi)
        self.assertAlmostEqual(area_circle(0), 0)
        self.assertAlmostEqual(area_circle(2.5), math.pi * 2.5 * 2.5)
    
    def test_perimeter_circle(self):
        self.assertAlmostEqual(perimeter_circle(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter_circle(0), 0)
        self.assertAlmostEqual(perimeter_circle(2.5), 2 * math.pi * 2.5)
    
    def test_area_square(self):
        self.assertEqual(area_square(1), 1)
        self.assertEqual(area_square(0), 0)
        self.assertEqual(area_square(4), 16)
    
    def test_perimeter_square(self):
        self.assertEqual(perimeter_square(1), 4)
        self.assertEqual(perimeter_square(0), 0)
        self.assertEqual(perimeter_square(4), 16)

if __name__ == "__main__":
    unittest.main()
