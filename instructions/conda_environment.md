# Travis CI to run and test a simple "Calculator" program in an Anaconda virtual environment

## Sign in to GitHub
* If you **do not** have an account, visit [GitHub](https://github.com/) and create a free account.
* In case you have an account, sign-in to your [GitHub](https://github.com/) account.

## Create a new repository
* In the upper-right corner of your GitHub page, use the **+** drop-down menu, and select New repository.
* Type a short, memorable name for your repository. For example, "travis-lab."
* Optionally, add a description of your repository. For example, "Repository to set up Travis CI on GitHub."
* Choose the repository visibility. **Note:** Travis CI provides special credits per month assigned to run builds only on public repositories ([Link](https://docs.travis-ci.com/user/billing-faq/#what-if-i-am-building-open-source)).
* Select **Initialize this repository with a README.**
* Click **Create repository.**

## Clone your fork locally
* Run the following command in the command prompt:

```
$ git clone https://USERNAME@github.com/USERNAME/travis-lab
$ cd travis-lab
```

In the above text, replace `USERNAME` with your GitHub user name.

## Create a simple "Calculator" program
* Create a short Python script named `calculator.py` in your repository with the following content:

```
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
                  Difference of the two numbers
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
```

* Add and commit the above new file to your repository and push the changes to GitHub:

```
$ git add calculator.py
$ git commit -m "Added Python Script."
$ git push origin master
```

* Visit your repository to confirm that your repository now contains the script `calculator.py`.

## Test the simple "Calculator" program with Pytest and Pytest-cov
*To be added*