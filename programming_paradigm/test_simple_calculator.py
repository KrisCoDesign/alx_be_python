import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -5), -6)
        # Add more assertions to thoroughly test the add method.

        # Remember to write additional test methods for subtract, multiply, and divide.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(12, 4), 8)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(3, 3), 9)

    def test_division(self):
        self.assertEqual(self.calc.divide(20, 5), 4)
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertIsNone(self.calc.divide(10, 0))



