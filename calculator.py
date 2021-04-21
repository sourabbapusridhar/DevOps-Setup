# Implementation of a simple "Calculator" program
# The calculator consists of four functions: add, subtract, multiply and divide

def add(x, y):
    """
    Function to add two numbers

    Parameters
    ----------
    x   : int/float
          First number to be added
    y   : int/float
          Second number to be added

    Returns
    -------
    sum : int/float
          Sum of the two numbers
    """
    return (x + y)

def subtract(x, y):
    """
    Function to subtract two numbers

    Parameters
    ----------
    x           : int/float
                  First number to be subtracted
    y           : int/float
                  Second number to be subtracted

    Returns
    -------
    difference  : int/float
                  Difference between the two numbers
    """
    return (x - y)

def multiply(x, y):
    """
    Function to multiply two numbers

    Parameters
    ----------
    x       : int/float
              First number to be multiplied
    y       : int/float
              Second number to be multiplied

    Returns
    -------
    product : int/float
              Sum of the two numbers
    """
    return (x * y)

def divide(x, y):
    """
    Function to divide two numbers

    Parameters
    ----------
    x           : int/float
                  First number to be divided
    y           : int/float
                  Second number to be divided

    Returns
    -------
    quotient    : int/float
                  Sum of the two numbers
    """
    return (x / y)