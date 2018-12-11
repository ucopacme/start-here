Learning to Program in Python
=============================

Goals:

- Understand some basic python.  There is no way to realistically learn to
  program in python within a 3-hour workshop.  But we hope at least to get you
  started.

Prerequisites:

- Access to Linux Platform (e.g. CentOS, AWS Cloud9)



Use Python 3 Virtual Environment
--------------------------------

You will be working from your python3 virtual environment you set up in
the previous workshop `Linux Workstation Setup`_.

If you are working from a Cloud9 environment as ``ec2-user``, you will
want to create a python 3 virtual environment::

  $ which python3
  $ python3 -m venv ~/python3-venv
  $ source ~/python3-venv/bin/activate

You will also need to remove the ``python`` shell alias from you ``~/.bashrc``::

  $ unalias python
  $ grep -v "alias python" ~/.bashrc > ~/.bashrc


Tutorials
---------

Take your pick from the following suggestions.  They are all good.

With all the tutorials, you will get much more out of the workshop if
you run the examples yourself.


`The Official Python 3 Tutorial`_
*********************************

https://docs.python.org/3/tutorial/index.html

See how far you get. Start with section 3 - `An Informal Introduction to Python`_

Try to get through sections:

- 4 - `More Control Flow Tools`_
- 5 - `Data Structures`_


`Python for You and Me`_
************************

This one is my favorite.  Again just see how far you get.  Skip the sections
on `Installation` and `Using mu editor`.



Video Turorial
--------------

`Automate the Boring Stuff`_
****************************

Users can skip lesson 1.  This talks mostly about installing python.

The videos make use of a text editor name ``idle``.  But any text editor
will do.  Cloud9 users can just use the IDE.

Please use earphones if viewing this in class.



Additional Resources
--------------------

The source of truth - python.org:

- http://docs.python.org/

This is a nice listing of on-line learning sites.  Let us know if you find
one which is particularly useful to you:

- https://docs.python-guide.org/intro/learning/


On-line Classes
***************

- https://cs61a.org/
- https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/index.htm


Books
*****

- https://learnpythonthehardway.org/python3/
- https://realpython.com/best-python-books/





.. _`Linux Workstation Setup`: https://github.com/ucopacme/start-here/blob/master/one_day_workshops/linux_workstation_setup.rst
.. _The Official Python 3 Tutorial: https://docs.python.org/3/tutorial/index.html
.. _An Informal Introduction to Python: https://docs.python.org/3/tutorial/introduction.html
.. _More Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html
.. _Data Structures: https://docs.python.org/3/tutorial/datastructures.html

.. _The Official Python 3 Tutorial: https://docs.python.org/3/tutorial/index.html
.. _Python for You and Me: https://pymbook.readthedocs.io/en/latest/index.html
.. _Automate the Boring Stuff: https://www.youtube.com/playlist?list=PL0-84-yl1fUnRuXGFe_F7qSH1LEnn9LkW
