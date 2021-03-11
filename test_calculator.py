# CS362 test_calculator
# Alex Young
# 3/11/2021
# Run this file using python3 test_calculator.py
# This program holds funtions to unit test for the functions in calculator

import calculator


class TestCalculator:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

    def test_multiply(self):
        assert 6 == calculator.multiply(3, 2)
