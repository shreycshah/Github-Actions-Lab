import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import financial_calculator

class TestFinancialCalculator(unittest.TestCase):

    # ---------- Simple Interest ----------

    def test_simple_interest(self):
        self.assertEqual(financial_calculator.simple_interest(1000, 10, 2), 200)
        self.assertEqual(financial_calculator.simple_interest(5000, 5, 1), 250)

    def test_simple_interest_zero(self):
        self.assertEqual(financial_calculator.simple_interest(1000, 0, 5), 0)
        self.assertEqual(financial_calculator.simple_interest(0, 10, 5), 0)

    def test_simple_interest_invalid(self):
        with self.assertRaises(ValueError):
            financial_calculator.simple_interest(-1000, 10, 2)

    # ---------- Compound Interest ----------

    def test_compound_interest(self):
        result = financial_calculator.compound_interest(1000, 10, 2)
        self.assertEqual(round(result, 2), 210.00)

    def test_compound_interest_zero_rate(self):
        self.assertEqual(financial_calculator.compound_interest(1000, 0, 5), 0)

    def test_compound_interest_invalid(self):
        with self.assertRaises(ValueError):
            financial_calculator.compound_interest(-1000, 10, 2)

        with self.assertRaises(ValueError):
            financial_calculator.compound_interest(1000, 10, 2, 0)

    # ---------- EMI Calculator ----------

    def test_calculate_emi(self):
        emi = financial_calculator.calculate_emi(120000, 12, 12)
        self.assertEqual(round(emi, 2), 10661.85)

    def test_calculate_emi_zero_interest(self):
        self.assertEqual(
            financial_calculator.calculate_emi(120000, 0, 12),
            10000
        )

    def test_calculate_emi_invalid(self):
        with self.assertRaises(ValueError):
            financial_calculator.calculate_emi(-120000, 12, 12)

        with self.assertRaises(ValueError):
            financial_calculator.calculate_emi(120000, 12, 0)

    # ---------- Profit or Loss Percentage ----------

    def test_profit_or_loss(self):
        self.assertEqual(
            financial_calculator.profit_or_loss_percentage(100, 120),
            20.0
        )
        self.assertEqual(
            financial_calculator.profit_or_loss_percentage(200, 150),
            -25.0
        )

    def test_profit_or_loss_invalid(self):
        with self.assertRaises(ValueError):
            financial_calculator.profit_or_loss_percentage(0, 100)

    # ---------- Discounted Price ----------

    def test_discounted_price(self):
        self.assertEqual(
            financial_calculator.discounted_price(1000, 10),
            900
        )
        self.assertEqual(
            financial_calculator.discounted_price(2000, 25),
            1500
        )

    def test_discounted_price_edge_cases(self):
        self.assertEqual(
            financial_calculator.discounted_price(1000, 0),
            1000
        )
        self.assertEqual(
            financial_calculator.discounted_price(1000, 100),
            0
        )

    def test_discounted_price_invalid(self):
        with self.assertRaises(ValueError):
            financial_calculator.discounted_price(-1000, 10)

        with self.assertRaises(ValueError):
            financial_calculator.discounted_price(1000, 120)


if __name__ == "__main__":
    unittest.main()