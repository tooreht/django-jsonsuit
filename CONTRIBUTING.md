# Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at <https://github.com/tooreht/django-jsonsuit/issues>.

If you are reporting a bug, please include:

-   Your operating system name and version.
-   Any details about your local setup that might be helpful in
    troubleshooting.
-   Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" is
open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with
"feature" is open to whoever wants to implement it.

### Write Documentation

django-jsonsuit could always use more documentation, whether as part of
the official django-jsonsuit docs, in docstrings, or even on the web in
blog posts, articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at
<https://github.com/tooreht/django-jsonsuit/issues>.

If you are proposing a feature:

-   Explain in detail how it would work.
-   Keep the scope as narrow as possible, to make it easier to
    implement.
-   Remember that this is a volunteer-driven project, and that
    contributions are welcome :)

## Get Started!

Ready to contribute? Here's how to set up django-jsonsuit for local
development.

1.  Fork the django-jsonsuit repo on GitHub.
2.  Clone your fork locally:

        $ git clone git@github.com:your_name_here/django-jsonsuit.git

3.  Install poetry

        $ python -m pip install poetry

4. Install poetry plugins

        $ poetry self add 'poethepoet[poetry_plugin]'
        $ poetry self add poetry-release

5. Install dependencies

        $ poetry install

6.  Create a branch for local development:

        $ git checkout -b name-of-your-bugfix-or-feature

    Now you can make your changes locally.

7.  When you're done making changes, check that your changes pass style
    and unit tests:

        $ poetry poe style
        $ poetry poe test

8. It is also possible to test other Python and Django versions with nox

        $ poetry run nox

9.  Commit your changes and push your branch to GitHub:

        $ git add .
        $ git commit -m "Your detailed description of your changes."
        $ git push origin name-of-your-bugfix-or-feature

10.  Submit a pull request through the GitHub website.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1.  The pull request should include tests.
2.  If the pull request adds functionality, the docs should be updated.
    Put your new functionality into a function with a docstring, and add
    the feature to the list in README.md.
3.  The pull request should work for Python 3.9, 3.10, 3.11 and for
    PyPy. Check <https://github.com/tooreht/django-jsonsuit/actions>
    and make sure that the tests pass for all supported Python versions.
