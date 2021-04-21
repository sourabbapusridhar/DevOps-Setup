# Implementation to test a simple "Calculator" program

import pytest
import calculator

def test_addition():
    """
    Unit test to test addition function from  the "Calculator" program
    The unit test tests output for both positive and negative int and float inputs

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    assert calculator.add(7, 3) == 10
    assert calculator.add(7.0, 3.0) == 10.0
    assert calculator.add(7, -3) == 4
    assert calculator.add(7.0, -3.0) == 4.0

def test_subtraction():
    """
    Unit test to test subtraction function from  the "Calculator" program
    The unit test tests output for both positive and negative int and float inputs

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    assert calculator.subtract(7, 3) == 4
    assert calculator.subtract(7.0, 3.0) == 4.0
    assert calculator.subtract(7, -3) == 10
    assert calculator.subtract(7.0, -3.0) == 10.0

def test_multiplication():
    """
    Unit test to test multiplication function from  the "Calculator" program
    The unit test tests output for both positive and negative int and float inputs

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    assert calculator.multiply(7, 3) == 21
    assert calculator.multiply(7.0, 3.0) == 21.0
    assert calculator.multiply(7, -3) == -21
    assert calculator.multiply(7.0, -3.0) == -21.0

def test_division():
    """
    Unit test to test division function from  the "Calculator" program
    The unit test tests output for both positive and negative int and float inputs
    The unit test also tests for ZeroDivisionError exception when divided by zero

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(10.0, 2.0) == 5.0
    assert calculator.divide(10, -2) == -5
    assert calculator.divide(10.0, -2.0) == -5.0

    with pytest.raises(ZeroDivisionError) as err:
        calculator.divide(1, 0)
    assert str(err.value) == "division by zero"

    with pytest.raises(ZeroDivisionError) as err:
        calculator.divide(1.0, 0.0)
    assert str(err.value) == "float division by zero"