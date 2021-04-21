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
* Run the following command in the terminal:

```
$ git clone https://USERNAME@github.com/USERNAME/travis-lab
$ cd travis-lab
```

In the above text, replace `USERNAME` with your GitHub user name.

## Create a simple "Calculator" program
* Create a Python file named `calculator.py` in your repository with the following content:

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
```

* Add and commit the above new file to your repository and push the changes to GitHub:

```
$ git add calculator.py
$ git commit -m "Added Python File."
$ git push origin master
```

* Visit your repository to confirm that your repository now contains the file `calculator.py`.

## Test the simple "Calculator" program with Pytest and Pytest-cov
* To test the simple "Calculator" program with Pytest and Pytest-cov, the packages Pytest and Pytest-cov must be installed. To install the python packages, run the following command in the terminal:

```
$ pip install pytest
$ pip install pytest-cov
```

* Create a Python file named `test_calculator.py` in your repository with the following content:

```
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
```

**Important:** The tutorial assumes that the prior knowledge to unit test a Python file with Pytest is already available. In case additional information is needed, please refer to the [Effective Python Testing With Pytest tutorial](https://realpython.com/pytest-python-testing/). Additionally, the prefix `test_` is essential in the filename `test_calculator.py` to ensure that the Pytest package recognizes the file `test_calculator.py` as a valid unit test file.

* Add and commit the above new file to your repository and push the changes to GitHub:

```
$ git add test_calculator.py
$ git commit -m "Added Python Unit Test File."
$ git push origin master
```

* Visit your repository to confirm that your repository now contains the file `test_calculator.py`.

## Sign in to Travis CI
* Since you already have a GitHub account, create a Travis CI account by visiting [Travis CI](https://travis-ci.com/) and selecting [Sign up with GitHub](https://travis-ci.com/signin).
* Accept the Authorization of Travis CI. You'll be redirected to GitHub.
* Click on your profile picture in the top right of your Travis Dashboard, click Settings and then the green Activate button, and select the repositories you want to use with Travis CI.

## Create a `.travis.yml` job file
* Add a `.travis.yml` file on the top level of your repository to tell Travis CI what to do. This file informs Travis CI on how to build and test your software. In addition, this file can also be used to specify any dependencies you need to install before building or testing your software. Create a `.travis.yml` file in your repository with the following content:

```
# Config file to run and test a simple "Calculator" program in an Anaconda virtual environment with Travis CI

language: python

python:
 - "3.6"

install:
 - wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
 - bash miniconda.sh -b -p $HOME/miniconda
 - source "$HOME/miniconda/etc/profile.d/conda.sh"
 - hash -r
 - conda config --set always_yes yes --set changeps1 no
 - conda update -q conda
 - conda info -a

before_script:
 - conda create -q -n test-environment python=$TRAVIS_PYTHON_VERSION pip
 - conda activate test-environment
 - pip install pytest
 - pip install pytest-cov

script:
 - pytest -v test_calculator.py --cov=calculator
```

The above file informs Travis CI to install miniconda, set up an anconda virtual environment named `test-environment` based on Python 3.6 environment, install required packages, activate virtual environemnt and run unit tests and test coverage on the `calculator.py` file.

* Add and commit the above new file to your repository and push the changes to GitHub to trigger a Travis CI build. Travis only runs builds on the commits you push after adding the `.travis.yml` file.

```
$ git add .travis.yml
$ git commit -m "Added Travis CI job file."
$ git push origin master
```

* Check the build status page to see if your build passes or fails according to the build command's return status by visiting [Travis CI](https://travis-ci.com/) and selecting your repository.

## Add a `README.md` file with a build status icon
* Each Travis CI job has an associated build status icon (e.g., [https://travis-ci.org/USERNAME/travis-lab.svg?branch=master](https://travis-ci.org/USERNAME/travis-lab.svg?branch=master)). The status icon can be embedded into the `README.md` file in a Git repository so that the current status of the build is always visible on viewing the Git repository via GitHub's web interface. To add the build status icon, add the following content in the `README.md` file:

```
# README for travis-lab

[![Build status](https://travis-ci.org/USERNAME/travis-lab.svg?master)](https://travis-ci.org/USERNAME)
```

The above text is a MarkDown syntax that specifies a hyperlink to [https://travis-ci.org/USERNAME](https://travis-ci.org/USERNAME) that is rendered as an SVG image, whose source is at [https://travis-ci.org/USERNAME/travis-lab.svg?master](https://travis-ci.org/USERNAME/travis-lab.svg?master).

* Add and commit the above changes to your repository and push the changes to GitHub to trigger a new Travis CI build. 

```
$ git add README.md
$ git commit -m "Added Travis CI build status icon to README."
$ git push origin master
```

## Acknowledgments
The instructions in this document are modified from [Travis CI Docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/use-conda-with-travis-ci.html).