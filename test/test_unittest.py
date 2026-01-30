import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 4), 6)
        self.assertEqual(calculator.fun1(5, 2), 7)
        self.assertEqual(calculator.fun1(-2, 2), 0)
        self.assertEqual(calculator.fun1(-1, -2), -3)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 4), -2)
        self.assertEqual(calculator.fun2(6, 0), 6)
        self.assertEqual(calculator.fun2(-1, 2), -3)
        self.assertEqual(calculator.fun2(-5, -5), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 4), 8)
        self.assertEqual(calculator.fun3(0, 5), 0)
        self.assertEqual(calculator.fun3(-1, 5), -5)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(10, 2), 5)
        self.assertEqual(calculator.fun5(5, 2), 2.5)
        self.assertEqual(calculator.fun5(-6, 3), -2)

        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(5, 0)

        with self.assertRaises(ValueError):
            calculator.fun5("a", 2)

    def test_fun6(self):
        self.assertEqual(calculator.fun6(2), 4)
        self.assertEqual(calculator.fun6(-3), 9)
        self.assertEqual(calculator.fun6(0), 0)
        self.assertEqual(calculator.fun6(2.5), 6.25)

        with self.assertRaises(ValueError):
            calculator.fun6("a")

    def test_fun7(self):
        self.assertEqual(calculator.fun7(0), 1)
        self.assertEqual(calculator.fun7(1), 1)
        self.assertEqual(calculator.fun7(5), 120)

        with self.assertRaises(ValueError):
            calculator.fun7(-1)

        with self.assertRaises(ValueError):
            calculator.fun7(2.5)

    def test_fun8(self):
        self.assertEqual(calculator.fun8(0), 1)
        self.assertEqual(calculator.fun8(1), 1)
        self.assertEqual(calculator.fun8(4), 24)

        with self.assertRaises(ValueError):
            calculator.fun8(-3)

        with self.assertRaises(ValueError):
            calculator.fun8("5")

    def test_fun9(self):
        self.assertEqual(calculator.fun9(2, 3), 8)
        self.assertEqual(calculator.fun9(5, 0), 1)
        self.assertEqual(calculator.fun9(2, -2), 0.25)
        self.assertEqual(calculator.fun9(2.5, 2), 6.25)

        with self.assertRaises(ValueError):
            calculator.fun9("a", 2)

        with self.assertRaises(ValueError):
            calculator.fun9(2, 2.5)

    def test_fun10(self):
        self.assertEqual(calculator.fun10(3, 2), 9)
        self.assertEqual(calculator.fun10(10, 1), 10)
        self.assertEqual(calculator.fun10(4, 0), 1)

        with self.assertRaises(ValueError):
            calculator.fun10("x", 2)

        with self.assertRaises(ValueError):
            calculator.fun10(2, "y")

if __name__ == "__main__":
        unittest.main()