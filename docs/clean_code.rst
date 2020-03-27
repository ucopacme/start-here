Clean Code
==========

"Software is the most complex thing that humans have ever attempted."
-- Jerry Weinberg

"Everything takes 3 times longer than you thing it will, even when you know this
and take it into account."

"We have a deadline.  I don't have time for clean code."




Some online resources about XP TDD and Clean Code
--------------------------------------------------


On Extreme Programming http://www.extremeprogramming.org/introduction.html

focus on sections: Designing, Coding, Testing http://www.extremeprogramming.org/rules.html

Video about XP https://www.youtube.com/watch?v=1FLaxNvmCc8


Clean Code per Robert Martin
----------------------------

The Book https://www.investigatii.md/uploads/resurse/Clean_Code.pdf

Robert Martin on Clean Architecture:
https://www.youtube.com/watch?v=o_TH-Y78tt4

46 Robert C Martin Clean Code III (skip to minute 20):
https://www.youtube.com/watch?v=QedpQjxBPMA&list=PLlu0CT-JnSasQzGrGzddSczJQQU729

Robert Martin "What Killed Smalltalk Could Kill Ruby, Too"
https://www.youtube.com/watch?v=YX3iRjKj7C0

in fact, anything you can find by Robert Martin
https://www.youtube.com/playlist?list=PLcr1-V2ySv4Tf_xSLj2MbQZr78fUVQAua


short videos on clean code
--------------------------

10 quick tips for making your code clean: https://www.youtube.com/watch?v=UjhX2sVf0eg

  1. You're responsible for code quality.
  #. Use meaningful names.
  #. Write code that expresses intent.
  #. Code should speak for itself. Less comments = less maintenance.
  #. Leave the code better than you found it.
  #. Single-responsibility code.  ie function does 1 thing well. Less arguments =
     better function.  casses. most methods use most of the class' properties.
  #. Tests (TDD).
  #. Work on big picture skeleton, then fill in the details later (nterface
     first, implementation later).
  #. Independent components that can be used in different places.
  #. Master your craft.

Tips for cleaner code: Cleaning up IF statements: https://www.youtube.com/watch?v=ldqDpmMkXgw




python style guides:
--------------------

https://github.com/google/styleguide/blob/gh-pages/pyguide.md
https://cs61a.org/articles/composition.html

http://downloads.niceware.com/TECH-pdf/PythonStyle-Writing_idiomatic_python_3.pdf



The Zen of Python
-----------------

https://www.python.org/dev/peps/pep-0020/

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

  Although practicality beats purity.

Errors should never pass silently.

  Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

  Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!




Some attributes of clean code
-----------------------------

Functions:

- every line is a function stays at the same level of abstraction, and that
  level is one below the name of the function.


- function should be smaller than a screen full (25 lines)

- a function should do one thing.  if it is possible to extract one function
  from another, the original function did more than one thing. - extract til
  you drop.

- a fully extracted function:
  
  - will have at most 2 levels of indentation.
  - the body of an if/while/for statement will be a function call
  - the predicate of an if/while/for statement will be a function call
  - the logic of the function reads like a sentence (since called functions have meaningful names)

- function should have at most 3 arguments

- function args should not be used to capture outputs

- do not use booleans as arguments.  make 2 separate functions instead

- function should expose outputs as return values.

- function should do just one thing - no side effects


names:

- function names should be verbs which clearly describe what a function does.

- the length of a variable name should be proportional to the scope in which that variable is active.

- the larger the scope of a function the shorter we want that name

  functions at broad scope (very general) should have short names.
  names get longer as scope gets smaller
