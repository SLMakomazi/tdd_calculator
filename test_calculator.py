import unittest
from calculator import add, multiply, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_multiple_numbers(self):
        self.assertEqual(add(1, 2, 3, 4, 5), 15)
        
    def test_multiply_two_numbers(self):
        self.assertEqual(multiply(1, 3), 3)
        self.assertEqual(multiply(-1, 3), -3)
        
    def test_multiply_multiple_numbers(self):
        self.assertEqual(multiply(1, 2, 3, 4, 5), 120)

    def test_subtract_two_numbers(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 3), -2)
        
    def test_subtract_multiple_numbers(self):
        self.assertEqual(subtract(10, 2, 3), 5)
        
    def test_divide_two_numbers(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(5, 2), 2.5)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
