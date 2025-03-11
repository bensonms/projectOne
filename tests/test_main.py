"""
Unit tests for the main module.
"""

import pytest
from projectone.main import add_numbers
from projectone.calculator import Calculator
from projectone.logger import Logger


@pytest.mark.add_numbers
def test_add_numbers():
    """Test the add_numbers function."""
    # Test with positive integers
    assert add_numbers(1, 2) == 3
    
    # Test with negative integers
    assert add_numbers(-1, -2) == -3
    
    # Test with mixed integers
    assert add_numbers(-5, 10) == 5
    
    # Test with floats
    assert add_numbers(1.5, 2.5) == 4.0


def test_add_numbers_edge_cases():
    """Test the add_numbers function with edge cases."""
    # Test with zero
    assert add_numbers(0, 0) == 0
    
    # Test with large numbers
    assert add_numbers(1000000, 2000000) == 3000000


# Use Logger class instead of MockLogger for testing
def test_calculator_add():
    """Test the Calculator add method."""
    # Create a logger
    logger = Logger()
    
    # Create calculator with injected logger
    calculator = Calculator(logger)
    
    # Test addition
    result = calculator.add(5, 3)
    
    # Assert the result
    assert result == 8
    
    # Assert the logging
    assert logger.logs[0] == "Added 5 and 3 to get 8"


def test_calculator_subtract():
    """Test the Calculator subtract method."""
    # Create a logger
    logger = Logger()
    
    # Create calculator with injected logger
    calculator = Calculator(logger)
    
    # Test subtraction
    result = calculator.subtract(10, 4)
    
    # Assert the result
    assert result == 6
    
    # Assert the logging
    assert logger.logs[0] == "Subtracted 4 from 10 to get 6"
