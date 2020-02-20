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
************************************

Recreate the following PDFs using reStructuredText.

- `Simple Document Example <autodoc/simple.pdf>`_
- `Harder Document Example <autodoc/harder.pdf>`_


Once you have them looking good, make a directory called ``my_project`` and
save them ``.rst`` files there.  We will use them in the next section.



Sphinx
------

Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation.  It was originally created for the Python documentation, and it
has excellent facilities for the documentation of software projects in a range
of languages.

Perform the tasks in this section from within your python virtual
environnment.

Sphinx Documentation:

- http://www.sphinx-doc.org/en/master/
- http://www.sphinx-doc.org/en/master/usage/quickstart.html
- https://matplotlib.org/sampledoc/


Getting Started Tutorial:

- https://matplotlib.org/sampledoc/getting_started.html


Initial sphinx setup
********************

Install sphinx python package::

  $ pip install  sphinx sphinx-autobuild

Create your docs project directory::

  $ mkdir -p my_project/docs
  $ cd my_project/docs

Initialize your sphinx project. you will be asked a lot of config questions.
You can just go with the offered defaults, but you will have to supply 
values for supply a **Project name** (``my-project``) and **Author name**::

  $ sphinx-quickstart 
  $ ls -l
  $ cat index.rst 


Build your site by running the ``make`` command::  

  $ make html

You should now be able to view the rendered website from a browser at ``docs/_build/html/index.html``


Adding pages to your site
*************************

Copy your ``.rst`` files from the previous section into your ``docs/`` 
directory::

  $ cp ~/simple.rst ~/harder.rst docs/

Setup links to these docs in the ``index.rst`` file.  Add the filenames
minus the ``.rst`` suffix below the ``toctree`` keyword.  Be sure they
are indented properly::

  Welcome to MyProject's documentation!
  ================================
  
  .. toctree::
     :maxdepth: 2
     :caption: Contents:
  
     simple
     harder

Rebuild your site and view from a browser as before::

   $ make html



Hosting your Site on readthedocs.io
-----------------------------------

GitHub Setup
************

Change directory into your ``my_project`` directory and initialize a
git repository.  ::

  $ cd my_project
  $ git init

Create a ``.gitignore`` file with the following contents::

  docs/_build

Commit your project into your new git repo::

  $ git add .
  $ git commit -m "Initial Commit of my_project"


If you do not already have a personal account on GitHub, do so now.  Go to
https://github.com/ and select **Sign up for Github**.

On GitHub create a new repository with the same name as your local repo.
Get the clone URL for the new repo (either ``ssh`` or ``https`` is ok).

Back in your local repo, define your GitHub repo as a remote repository and
syncronize your local repo contents with your remote::

  $ git remote add origin <clone URL>
  $ git push -u origin master


Read the Docs Setup
*******************

Edit your sphinx conf.py file.

set your ``index.rst`` as the ``master_doc``::

  master_doc = 'index'

set your sphinx theme to the ReadTheDocs theme (optional)::

  #html_theme = 'alabaster'
  import sphinx_rtd_theme
  html_theme = 'sphinx_rtd_theme'


Open the Read the Docs website at https://readthedocs.org and open the **login**
dialogue.  Select **Sign in with GitHub**.

Configure your new GitHub project as a Read the Docs project.  Select **Import
a Project**.  Read the Docs will scan your GitHub repositories.  This may
take a few seconds.  Hit the plus sign ``+`` next to your ``my_project``
repo.

The name of your project must be unique or you will get a build error.  So in the ``Name`` entry widget edit the project name to something other than ``my_project``.

Now select **Build version**.  This should generate html files from your sphinx
project and post them to a world accessible URL.  Once the build is finished
select **View Docs** in the upper left corner of your project page.  This 
should take you to ``https://<project_name>.readthedocs.io/en/latest/``.  
Your docs site is live!

Make a change to one of your ``.rst`` files in your local repo.  Commit the
change and push to your remote.  Read the Docs will notice the new version and
automatically rebuild your project documentation.  In a few minutes you will
see your change on your project URL.

Sweet!



Configure Sphinx with AutoAPI Extention - Extra Credit
------------------------------------------------------

To get RTD to autobuild API docs from your python module doc strings use the
autoapi extention.  Once this is configured you do not need to alter your
``index.rst`` file.  The extention adds its own ``toctree`` for you.

For autoapi to source your docstrings, it must import your modules.
So you may have to tweek advances settings in RTD to builds with python 3.

On your Read the Docs project page select ``Admin -> Advanced Settings``.
In the ``Python Interpreter`` dropdown select ``cpython 3.x```.


Install sphinx-autoapi::

  > pip install sphinx-autoapi


add sphinx and sphinx-autoapi to ``requirements.txt``::

  > cat requirements.txt 
  pytest
  pytest-cov
  flake8
  sphinx
  sphinx-autoapi


In ``docs/conf.py``::

  # Add any Sphinx extension module names here, as strings. They can be
  # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
  # ones.
  extensions = [
      'autoapi.extension',
      'sphinx.ext.napoleon',
  ]
  
  # Document Python Code - for use with autoapi.extension
  autoapi_type = 'python'
  autoapi_dirs = ['../organizer']




