Automating Project Documentation
================================

This workshop focuses on the use of open source documentation tools to
generate on-line documentation of your python project.

Goals:

- basic command of reStructuredText
- ability to build doc site with Sphinx
- self-documentation of python code using docstrings

Prerequisites:

- access to unix bash shell
- basic command of git
- personal account on github
- some familiarity with python is helpful


reStructuredText
----------------

We use reStructuredText markup for project documentation.

reStructuredText is an easy-to-read, what-you-see-is-what-you-get plaintext
markup syntax and parser system. It is useful for in-line program
documentation, for quickly creating simple web pages, and for standalone
documents.

The primary goal of reStructuredText is to define and implement a markup
syntax for use in Python docstrings and other documentation domains,
that is readable and simple, yet powerful enough for non-trivial use.

For example, if there is a ``README.rst`` file in the root directory of a git
repository, GitHub will automatically render it as html and display it.

In fact, the page you are reading now was composed in reStructuredText.
If you are viewing this document on GitHub, click on the **Raw** tab 
in the upper right hand corner to see the underlying markup.


Composing Docs with reStructuredText
************************************

To get started with reStructuredText markup, read through `A ReStructuredText
Primer <http://docutils.sourceforge.net/docs/user/rst/quickstart.html>`_.

For additional documentation:

- http://docutils.sourceforge.net/docs/user/rst/quickref.html
- http://docutils.sourceforge.net/rst.html

There is a simple on-line reStructuredText editor you can use to view
rendered markup in real time: http://rst.ninjs.org.  Type or paste your
markup on the left-hand side, and see the rendered result (or error messages)
on the right-hand side. Sweet!

Another useful tool is the ``rst2html`` command.  This takes reStructuredText
file as and argument and renders html code to STDOUT.  It warns of syntax
errors.  Redirect the output to a temp `.html` file and point your browser at
it.  If you are working from a Cloud9 environment, left-click on the ``.html``
file and select **Preview**::

  $ rst2html my_doc.rst > /tmp/my_doc.html



reStructuredText Workshop Assignment
------------------------------------

Recreate the following ``.html`` pages using reStructuredText.

- `Simple Document Example <rst_samples/simple.html>`_
- `Harder Document Example <rst_samples/harder.html>`_




