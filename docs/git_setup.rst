Setting up Git
==============

Git Environment
---------------

Ensure your git commit messages contain correct contact info::

  git config --global user.name "Ashley Gould"
  git config --global user.email "agould@ucop.edu"

Ensure vim is your default editor for git commit messages::

  git config --global core.editor /usr/bin/vim

Ensure git tab completion is enabled.  Git comes with its own auto-completion script, so if tab completion is not enabled, usually all you need is to set up bash-completion. (https://github.com/bobthecow/git-flow-completion/wiki/Install-Bash-git-completion)::

  # fedora
  sudo dnf install bash-completion
  . ~/.bashrc

  # centos
  sudo yum install bash-completion
  . ~/.bashrc

  # debian
  sudo apt-get install bash-completion
  . ~/.bashrc


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
or STS tokens.  There are pros and cons to CodeCommit:

Pros:

- access to repos is controled by IAM user auth and policies - very secure
- integrates well with other AWS services
- very reliable

Cons:

- repositories can not be made publicly accessible
- cross-account access to repos is difficult to configure
- does not itegrate will with some IDEs when using access keys or STS tokens
- commandline access requires additional git config setup 


CodeCommit credential-helper setup
----------------------------------

To access codecommit repositories from the commandline, you must first
configure git environment to use the AWS CodeCommit ``credential-helper``.  Run
the following commands::

  git config --global credential.helper '!aws codecommit credential-helper $@'
  git config --global credential.UseHttpPath true

