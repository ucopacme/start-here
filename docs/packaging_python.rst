Packaging Python
================


Packaging
---------


these 2 are the same site:

- http://python-packaging-user-guide.readthedocs.io/
- https://packaging.python.org/


building and packaging python projects:

https://packaging.python.org/tutorials/packaging-projects/

create an account for yourself at https://test.pypi.org/

::

  > pip install -U pip setuptools wheel
  > pip install twine

  > python setup.py sdist bdist_wheel
  [cut]
  > ls dist/
  orgcrawler-1.0.0a1-py3-none-any.whl  orgcrawler-1.0.0a1.tar.gz

  > python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  Enter your username: agould
  Enter your password:
  Uploading distributions to https://test.pypi.org/legacy/
  Uploading orgcrawler-1.0.0a1-py3-none-any.whl
  100%|████████████████████████████████████████████████| 34.5K/34.5K [00:02<00:00, 16.3KB/s]
  Uploading orgcrawler-1.0.0a1.tar.gz
  100%|████████████████████████████████████████████████| 22.3K/22.3K [00:01<00:00, 15.7KB/s]


if the upload errors out because of setup.py syntax, be sure to rerun the dist build
again before retrying the upload::

  > python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  Enter your username: agould
  Enter your password:
  Uploading distributions to https://test.pypi.org/legacy/
  Uploading orgcrawler-1.0.0a1-py3-none-any.whl
  100%|████████████████████████████████████████████████| 34.5K/34.5K [00:00<00:00, 61.2KB/s]
  NOTE: Try --verbose to see response content.
  HTTPError: 400 Client Error: "['agould@ucop.edu', 'santhosh.katakam@ucop.edu']" is an invalid value for Author-email. Error: Use a valid email address See https://packaging.python.org/specifications/core-metadata for url: https://test.pypi.org/legacy/
  (python3.6) agould@horus:~/git-repos/github/ucopacme/orgcrawler> python setup.py sdist bdist_wheel
  running sdist
  [cut]


test the install::

  > pip install -i https://test.pypi.org/simple/ --no-deps orgcrawler
  Looking in indexes: https://test.pypi.org/simple/
  Collecting orgcrawler
    Downloading https://test-files.pythonhosted.org/packages/53/54/87c044d38bcbfa7289158f402637dad402b9fc9b3deed490ebe8230a4675/orgcrawler-1.0.0a1-py3-none-any.whl
  Installing collected packages: orgcrawler
  Successfully installed orgcrawler-1.0.0a1


Now publish to real pypi.  create an account at https://pypi.org::

  > python -m twine upload dist/*
  Enter your username: agould
  Enter your password: 
  Uploading distributions to https://upload.pypi.org/legacy/
  Uploading orgcrawler-1.0.0a1-py3-none-any.whl
  100%|████████████████████████████████████████████████| 34.5K/34.5K [00:02<00:00, 16.2KB/s]
  Uploading orgcrawler-1.0.0a1.tar.gz
  100%|████████████████████████████████████████████████| 22.3K/22.3K [00:01<00:00, 15.1KB/s]
  
  > pip search orgcrawler
  orgcrawler (1.0.0a1)  - Tools for working with AWS Organizations
    INSTALLED: 1.0.0a1 (latest)



understaning setup.py:
https://packaging.python.org/guides/distributing-packages-using-setuptools/


https://packaging.python.org/specifications/core-metadata


understanding classifiers
https://pypi.org/classifiers/


Understanding Release Numbers
-----------------------------

Semantic
********

https://semver.org/

Given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when you make incompatible API changes,
- MINOR version when you add functionality in a backwards-compatible manner, and
- PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

See the faq for more details.


PEP 440
*******

https://www.python.org/dev/peps/pep-0440/

Within a numeric release, the following suffixes are permitted and MUST be ordered as shown::

  .devN, aN, bN, rcN, <no suffix>, .postN

  X.YdevN    # Development release
  X.YaN      # Alpha release
  X.YbN      # Beta release
  X.YrcN     # Release Candidate
  X.Y        # Final release
  X.Y.postN  # Post release 


Release Types
*************

https://en.wikipedia.org/wiki/Software_release_life_cycle

Development release
  early releases created directly from source control which do not conflict with later project releases.

Alpha release
  product feature which you are developing is incomplete or partially complete. 

Beta release
  product feature is complete or development is done, but it could contain some bugs and performance issues.

Release candidate
  beta version with potential to be a final product, which is ready to release unless significant bugs emerge.

Post release
  for minor errors in a final release that do not affect the distributed
  software (for example, correcting an error in the release notes).


Examples
********

::

  1.0.dev1
  1.0.dev2
  1.0a1
  1.0a2
  1.0b1
  1.0b2
  1.0rc1
  1.0rc2
  1.0
  1.0.post1
  1.0.post2
  1.1.dev1




Publishing
----------

Generate distribution packages for the package, and push to PyPi.

PyPI docs:
https://packaging.python.org/tutorials/packaging-projects/

Create yourself an account on PyPi, the Python Package Index:
https://pypi.org/account/register/

Aslo create yourself an account on the test PyPi:
https://test.pypi.org/account/register/


Make sure your python environment has required tools::

  pip install --upgrade setuptools wheel twine

Now run this command from the same directory where setup.py is located:: 

  cd aws-orgs
  python setup.py sdist bdist_wheel

Once completed this command should generate two files in the dist directory::

  aws-orgs> ls -1 dist/
  aws_orgs-0.2.0-py3-none-any.whl
  aws-orgs-0.2.0.tar.gz


Run Twine to upload all of the archives under dist.

First, just upload to test.pypi.org::

  twine upload --repository-url https://test.pypi.org/legacy/ dist/*

Once uploaded your package should be viewable on TestPyPI, for example, https://test.pypi.org/project/aws-orgs

You can use pip to install your package and verify that it works. Create a new
virtualenv and install your package from TestPyPI::

  python -m venv pypi_test
  source pypi_test/bin/activate
  pip install --index-url https://test.pypi.org/simple/ --no-deps aws-orgs
  deactivate
  rm -rf pypi_test/


Now upload to real PyPI::

  twine upload dist/*

---

need vetting
------------


https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
https://pypi.python.org/pypi?%3Aaction=list_classifiers

https://github.com/kennethreitz/setup.py/blob/master/setup.py

https://packaging.python.org/tutorials/installing-packages/

https://setuptools.readthedocs.io/en/latest/

# very nice
https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure



setup.py explain links:
-----------------------

http://peak.telecommunity.com/DevCenter/setuptools
https://manikos.github.io/how-pythons-import-machinery-works

