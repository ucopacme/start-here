Contributing to Github
======================

Contributing Code
-----------------

Contributions should be made in response to a particular GitHub Issue. We find it easier to review code if we've already discussed what it should do, and assessed if it fits with the wider codebase.


A good pull request:

* Is clear.
* Works across all supported version of Python (python 3.6).
* Complies with the existing codebase style (`flake8 <http://flake8.pycqa.org/en/latest/>`_).
* Includes `docstrings <https://www.python.org/dev/peps/pep-0257/>`_ and comments for unintuitive sections of code.
* Includes documentation for new features.
* Includes tests cases that demonstrates the previous flaw that now passes with the included patch, or demonstrates the newly added feature. Tests should have 100% code coverage.
* Is appropriately licensed (GPLv3).


Get Started
-----------

1. Fork the repository on GitHub.
2. Clone your fork locally::

    $ git clone git@github.org:<github_username>/my_project.git

3. For python projects install the package for development from your cloned repository (we recommend you use a `virtual environment <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_):

   .. code-block:: shell

    $ cd my_project/
    $ pip install -r requirements.txt
    $ pip install -e .

4. Create a branch for local development:

   .. code-block:: shell

    $ git checkout -b <branch-name>

5. When you're done making changes, check that your changes pass linting, unit-tests,  and that unit-tests have sufficient coverage:

   Check linting:
   .. code-block:: shell

      $ flake8

   Run unit tests or coverage in your current environment - (handy for quickly running unit tests):

   .. code-block:: shell

      $ pytest


6. Make sure the changes comply with the pull request guidelines in the section on `Contributing Code`_.

7. Commit and push your changes.

   Commit messages should follow `these guidelines <https://github.com/erlang/otp/wiki/Writing-good-commit-messages>`_.

   Use the following commit message format ``[Resolves #issue_number] Short description of change``.

   e.g. ``[Resolves #123] Fix description of resolver syntax in documentation``

8. Submit a pull request through the GitHub website.

