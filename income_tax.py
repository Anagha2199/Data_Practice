import unittest
def calculate_income_tax(income):
    """
    Function to calculate income tax based on income brackets.
    Assumes 2023 tax brackets for simplicity.
    """
    if income < 0:
        raise ValueError("Income cannot be negative.")
    elif income <= 10000:
        tax = 0.0
    elif income <= 40000:
        tax = (income - 10000) * 0.1
    elif income <= 80000:
        tax = 3000 + (income - 40000) * 0.2
    else:
        tax = 11000 + (income - 80000) * 0.3

    return tax

class TestIncomeTaxCalculation(unittest.TestCase):

    def test_tax_calculation(self):
        self.assertAlmostEqual(calculate_income_tax(5000), 0.0, places=2)
        self.assertAlmostEqual(calculate_income_tax(20000), 1000.0, places=2)
        self.assertAlmostEqual(calculate_income_tax(60000), 7000.0, places=2)
        self.assertAlmostEqual(calculate_income_tax(100000), 17000.0, places=2)

    def test_negative_income(self):
        with self.assertRaises(ValueError):
            calculate_income_tax(-5000)


if __name__ == "__main__":
    unittest.main()
