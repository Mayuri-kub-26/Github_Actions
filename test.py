import pytest
from main import add, subtract, multiply, divide


class TestArithmeticOperations:
    
    def test_add_pos_nums(self):
        assert add(5, 3) == 8
    
    def test_add_neg_nums(self):
        assert add(-5, -3) == -8
    
    def test_add_mixed_nums(self):
        assert add(5, -3) == 2
    
    def test_add_zero(self):
        assert add(0, 5) == 5
    
    def test_subtract_pos_nums(self):
        assert subtract(10, 3) == 7
    
    def test_subtract_neg_nums(self):
        assert subtract(-10, -3) == -7
    
    def test_subtract_mixed_nums(self):
        assert subtract(5, -3) == 8
    
    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
    
    def test_multiply_pos_nums(self):
        assert multiply(4, 5) == 20
    
    def test_multiply_neg_nums(self):
        assert multiply(-4, -5) == 20
    
    def test_multiply_mixed_nums(self):
        assert multiply(-4, 5) == -20
    
    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
    
    def test_divide_pos_nums(self):
        assert divide(10, 2) == 5
    
    def test_divide_neg_nums(self):
        assert divide(-10, -2) == 5
    
    def test_divide_mixed_nums(self):
        assert divide(-10, 2) == -5
    
    def test_divide_by_zero(self):
        assert divide(10, 0) == "Cannot divide by zero"
    
    def test_divide_zero_numerator(self):
        assert divide(0, 5) == 0
    
    def test_divide_decimals(self):
        assert divide(7.5, 2.5) == 3.0