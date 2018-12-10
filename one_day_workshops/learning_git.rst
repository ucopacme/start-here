Learning Git
=============

Goals:

- master basic git commands and workflow
- master basics of working with remote repositories
- introduction to codecommit and github

Prerequisites:

- Access to Linux Platform (e.g. CentOS, AWS Cloud9)


Cloud9 Setup
------------

If you are working from a cloud9 environment you may want to reset
your default editor to `vim` instead of `nano`::

  $ git config --global core.editor /usr/bin/vim

Also useful is git bash completion::

  $ sudo yum install bash-completion
  $ source ~/.bashrc

 
Git Tutorials
-------------

The meat-and-potatoes of this workshop consists of working through either
of two recommended git tutorials.  Chose whichever one suits your taste.

As you work the tutorials I highly recommend that you do not cut-and-paste, but
type out all commands.  This is a much more effective way to learn.  Make use
of tab completion.  Of course, this recommendation does not apply to sample file
content.


Ry’s Git Tutorial
*****************

https://web.archive.org/web/20161121145226/http://rypress.com:80/tutorials/git/index

This is a very clear and nicely organized on-line tutorial.  It covers basic
git commands and workflow first and then progresses to working with remote
repositories.

The original site is hosted from a web archive.  This creates some qwirks to be
aware of:

- Each chapter gets redirected to the archive site.  Expect a few seconds lag
  time for tutorial chapters to load.  For best results, open each chapter in a
  new tab.

- Some chapters ask you to download a demo repository.  The downloads are
  optional for in case you are starting from the middle of the tutorial.
  However, the download links are broken.  But, so long as you follow the
  tutorial from the begining, the repository you create and work from will be
  consistant with the tutorial instructions.


Official Git Tutorial
*********************

https://git-scm.com/docs/gittutorial

or from the bash shell::

  $ man gittutorial


This is a more complete tutorial, and it my not be quite as easy to follow as
Ry’s Git Tutorial.  But if you already know some basic git, you may find this
one to be more informative.  (There was some stuff I didn't know about!)

This tutorial also has a quirk:

- some of the examples ask you to run ``gitk``.  This is a GUI git repository
  viewer.  It is excellent, but most likely you will have to install it, and it
  will not work at all from your Cloud9 environment, because there is no way for
  you to export your display.  The workaround is to install and run ``tig``
  instead::

  $ sudo yum install tig
  $ cd my-git-repo
  $ tig



Github
------

If you don't already have one, create a personal git account for yourself.
Go to https://github.com/ and select **Sign up for Github**.

See the various github guides at https://guides.github.com/

For starters:

- https://guides.github.com/activities/hello-world/
- https://guides.github.com/introduction/git-handbook/


Also see the various Github help articles: https://help.github.com/


Once you create your Github account, we recommend you upload your ssh public
key into your github account.  This allows a more transparent workflow with
github repositories:
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/



CodeCommit
----------

AWS CodeCommit service hosts git repositories in your AWS accounts.  You 
authiticate to your repositories using your AWS credentials, access keys,
or STS tokens.  

To create a codecommit repository with AWS CLI::

  $ aws codecommit create-repository --repository-name my-git-repo

Use the value of cloneUrlHttp to clone this repo or to configure it as a
remote::

  $ aws codecommit get-repository --repository-name my-git-repo | grep cloneUrlHttp


CodeCommit credential-helper setup
**********************************

To access codecommit repositories from the commandline, you must first
configure git environment to use the AWS CodeCommit ``credential-helper``.  Run
the following commands::

  git config --global credential.helper '!aws codecommit credential-helper $@'
  git config --global credential.UseHttpPath true



CodeCommit Vs. Github
---------------------

There are pros and cons to CodeCommit as compared to Github:

Pros:

- access to repos is controled by IAM user auth and policies - very secure
- integrates well with other AWS services
- very reliable

Cons:

- repositories cannot be made publicly accessible
- cross-account access to repos is difficult to configure
- does not itegrate will with some IDEs when using access keys or STS tokens
- commandline access requires additional git config setup 



