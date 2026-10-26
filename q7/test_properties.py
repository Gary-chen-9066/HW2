import random
import unittest
from fractions import Fraction
from math import floor
from q7.Calc import Calculator

SEED = 2026
TRIALS = 500


def pairs(nonzero_b=False):
    rng = random.Random(SEED)
    for _ in range(TRIALS):
        a = rng.randint(-10**6, 10**6)
        b = rng.randint(-10**6, 10**6)
        if nonzero_b and b == 0:
            b = 1
        yield a, b


class TestCalculatorProperties(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtract_undoes_add(self):
        for a, b in pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.subtract(self.calc.add(a, b), b), a)

    def test_add_is_commutative(self):
        for a, b in pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    def test_multiply_is_commutative(self):
        for a, b in pairs():
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.multiply(a, b),
                                 self.calc.multiply(b, a))

    def test_multiply_is_repeated_add(self):
        for a, _ in pairs():
            with self.subTest(a=a):
                self.assertEqual(self.calc.multiply(a, 3),
                                 self.calc.add(self.calc.add(a, a), a))

    def test_divide_undoes_multiply(self):
        for a, b in pairs(nonzero_b=True):
            with self.subTest(a=a, b=b):
                self.assertEqual(
                    self.calc.divide(self.calc.multiply(a, b), b), a)

    def test_divide_is_floor_of_exact_quotient(self):
        for a, b in pairs(nonzero_b=True):
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.divide(a, b), floor(Fraction(a, b)))

    # Exposes an unspecified decision: the Q1 tests never fix how a
    # non-exact negative quotient rounds, and floor division is not
    # symmetric, e.g. divide(-5, 2) == -3 but -divide(5, 2) == -2.
    @unittest.expectedFailure
    def test_divide_negation_symmetry(self):
        for a, b in pairs(nonzero_b=True):
            self.assertEqual(self.calc.divide(-a, b), -self.calc.divide(a, b),
                             msg=f"a={a}, b={b}")


if __name__ == "__main__":
    unittest.main()
