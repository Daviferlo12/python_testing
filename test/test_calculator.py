import unittest
from src.calculator import(
    sum, substract, multiplication, division
)

class CalculatorTest(unittest.TestCase):
    
    def test_sum(self):
        assert sum(1,4) == 5
        
    def test_substract(self):
        assert  substract(5,1) == 4
        
    def test_multiplication(self):
        assert  multiplication(5,5) == 25
        
    def test_division(self):
        assert division(10,2) == 5
        
    def test_division_raise_error_zero_division(self):
        with self.assertRaises(ValueError):    
            division(10,0)