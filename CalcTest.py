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

    def test_multiply_negitive(self):
        calc = Calculator()
        result = calc.multiply(-3, 2)
        self.assertEqual(result, -6) 

    def test_multiply_zero(self):
        calc = Calculator()
        result = calc.multiply(3, 0)
        self.assertEqual(result, 0)
        
         
if __name__ == "__main__":
    unittest.main()