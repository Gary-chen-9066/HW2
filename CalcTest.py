import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(4, 1)
        self.assertEqual(result, 3)

    def test_multiply_positive(self):
        calc = Calculator()
        result = calc.multiply(3, 2)
        self.assertEqual(result, 6)

    def test_multiply_negative(self):
        calc = Calculator()
        result = calc.multiply(-3, 2)
        self.assertEqual(result, -6)

    def test_multiply_zero(self):
        calc = Calculator()
        result = calc.multiply(3, 0)
        self.assertEqual(result, 0)

    def test_divide_positive(self):
        calc = Calculator()
        result = calc.divide(4, 2)
        self.assertEqual(result, 2)

    def test_divide_negative(self):
        calc = Calculator()
        result = calc.divide(-4, 2)
        self.assertEqual(result, -2)

    def test_divide_zero(self):
        calc = Calculator()
        result = calc.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_nondivisible(self):
        calc = Calculator()
        result = calc.divide(5, 2)
        self.assertEqual(result, 2)

    def test_modulo_sign_follows_divisor(self):
        calc = Calculator()
        self.assertEqual(calc.modulo(7, 3), 1)
        self.assertEqual(calc.modulo(-7, 3), 2)
        self.assertEqual(calc.modulo(7, -3), -2)
        self.assertEqual(calc.modulo(-7, -3), -1)

    def test_modulo_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.modulo(7, 0)

    def test_power_zero_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(0, 0), 1)
        self.assertEqual(calc.power(5, 0), 1)

    def test_power_positive_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, 3), 8)
        self.assertEqual(calc.power(-2, 3), -8)
        self.assertEqual(calc.power(0, 2), 0)

    def test_power_negative_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.power(2, -1), 0.5)
        self.assertEqual(calc.power(2, -2), 0.25)
        self.assertEqual(calc.power(-2, -1), -0.5)
        self.assertIsInstance(calc.power(1, -1), float)

    def test_power_zero_base_negative_exponent(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.power(0, -1)


if __name__ == "__main__":
    unittest.main()
