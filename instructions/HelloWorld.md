# Travis CI for a simple "Hello World" program

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

## Create a "Hello World" program
* Create a short Python script named `hello.py` in your repository with the following content:

```
print("Hello World!")
```

* Test the script by running it once locally using command prompt:

```
$ python hello.py
Hello World!
```

* Add and commit the above new file to your repository and push the changes to GitHub:

```
$ git add hello.py
$ git commit -m "Added Python Script."
$ git push origin master
```

* Visit your repository to confirm that your repository now contains the script `hello.py`.

## Sign in to Travis CI
* Since you already have a GitHub account, create a Travis CI account by visiting [Travis CI](https://travis-ci.com/) and selecting [Sign up with GitHub](https://travis-ci.com/signin).
* Accept the Authorization of Travis CI. You'll be redirected to GitHub.
* Click on your profile picture in the top right of your Travis Dashboard, click Settings and then the green Activate button, and select the repositories you want to use with Travis CI.

## Create a `.travis.yml` job file
* Add a `.travis.yml` file to your repository to tell Travis CI what to do. This file informs Travis CI on how to build and test your software. In addition, this file can also be used to specify any dependencies you need to install before building or testing your software. Create a `.travis.yml` file in your repository with the following content:

```
language: python

python:
 - "3.6"

script:
 - python hello.py
```

The above file informs Travis CI to set up a Python 3.6 environment and run the `hello.py` script.

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
The instructions in this document are modified from ["Hello World" with Travis CI tutorial](https://github.com/softwaresaved/build_and_test_examples/blob/master/travis/HelloWorld.md), [GitHub Docs](https://docs.github.com/en) and [Travis CI Docs](https://docs.travis-ci.com/).