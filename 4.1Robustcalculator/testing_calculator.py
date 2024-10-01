import unittest
import math
from robustcalculator import RobustCalculator 

class TestRobustCalculator(unittest.TestCase):
    
    def setUp(self):
        # Initialize the calculator object before each test
        self.calculator = RobustCalculator()

    # 1. Test addition
    def test_add(self):
        self.assertEqual(self.calculator.add(3, 4), 7)
        self.assertEqual(self.calculator.add(-3, -4), -7)
        self.assertEqual(self.calculator.add(3, -4), -1)
        self.assertEqual(self.calculator.add(0, 5), 5)
        with self.assertRaises(TypeError):
            self.calculator.add("three", 4)

    # 2. Test subtraction
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 3), 7)
        self.assertEqual(self.calculator.subtract(-5, -2), -3)
        self.assertEqual(self.calculator.subtract(5, 0), 5)
        with self.assertRaises(TypeError):
            self.calculator.subtract(5, "two")

    # 3. Test multiplication
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-3, 4), -12)
        self.assertEqual(self.calculator.multiply(5, 0), 0)
        with self.assertRaises(TypeError):
            self.calculator.multiply("three", 4)

    # 4. Test division
    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, 2), -5)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)
        with self.assertRaises(TypeError):
            self.calculator.divide(10, "two")

    # 5. Test square root
    def test_square_root(self):
        self.assertEqual(self.calculator.square_root(16), 4)
        self.assertEqual(self.calculator.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calculator.square_root(-16)
        with self.assertRaises(TypeError):
            self.calculator.square_root("sixteen")

    # 6. Test exponentiate
    def test_exponentiate(self):
        self.assertEqual(self.calculator.exponentiate(2, 3), 8)
        self.assertEqual(self.calculator.exponentiate(-2, 3), -8)
        self.assertEqual(self.calculator.exponentiate(5, 0), 1)
        with self.assertRaises(TypeError):
            self.calculator.exponentiate(2, "three")

    # 7. Test logarithm
    def test_logarithm(self):
        self.assertAlmostEqual(self.calculator.logarithm(1), 0)
        self.assertAlmostEqual(self.calculator.logarithm(100, 10), 2)
        with self.assertRaises(ValueError):
            self.calculator.logarithm(-10)
        with self.assertRaises(TypeError):
            self.calculator.logarithm("ten")

    # 8. Test validate_input
    def test_validate_input(self):
        try:
            self.calculator.validate_input(5, 10)
        except Exception as e:
            self.fail(f"validate_input raised {e} unexpectedly!")
        
        with self.assertRaises(TypeError):
            self.calculator.validate_input(5, "ten")

if __name__ == '__main__':
    unittest.main()
