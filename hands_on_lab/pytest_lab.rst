Pytest Lab
==========


post to::

  user_solutions/$USER/pytest/lab_X/

Lab 1
-----
using pytest. writing assert statemests

- write test module ``test_lab_1.py``' with 2 functions::

  def test_hello_world():
      """asserts output of hello_world() is string 'hello world'"""

  def test_plus_four():
      """asserts output of plus_four(2) equals 6"""

- run pytest in same directory is ``test_lab_1.py``.  it should fail 2 tests

- now write python module ``lab_1.py`` to with 2 functions::

  def hello_world():
      """returns the string 'hello world'"""

  def plus_four(x):
      """returns x + 4"""

- run pytest in same directory is ``test_lab_1.py``.  it should pass 2 tests



