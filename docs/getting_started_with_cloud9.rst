Getting Started with Cloud9
===========================


Create a Cloud9 environment for yourself
----------------------------------------

Here is link to the Cloud9 tutorial 
https://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html

But here are the basics:

- assume role into your development account
- click on 'Services' tab
- type in 'cloud9' and press <Enter>
- validate you are in the correct region (UCOP default is 'Origon - us-west-2')
- press 'Create Environment'
- put your IAM user name in 'Name' field
- for all other options you can just use defaults
- click your way through the dialogs to create the environment



Clone Codecommit Repository into Cloud9 Environemt
--------------------------------------------------

From command prompt (at bottom of screen)::

  # configure git for codecommit access
  git config --global credential.helper '!aws codecommit credential-helper $@'
  git config --global credential.UseHttpPath true

  # install 'jq' tool (parses json objects)
  sudo yum install -y jq

  # list codecommit repos in this account and region
  aws codecommit list-repositories

  # get the clone url for a given repository name (example: "s-team")
  REPO_NAME=s-team
  CLONE_URL=$(aws codecommit get-repository --repository-name $REPO_NAME | jq .repositoryMetadata.cloneUrlHttp | tr -d '"')
  echo $CLONE_URL

  # clone the repo
  git clone $CLONE_URL


Add some other nice Cloud9 fixes
--------------------------------

From command prompt::

  # make python3 the default
  unalias python
  sudo alternatives --set python /usr/bin/python3.6
  
  # install boto3
  sudo pip install boto3
  
  # set up git/awscli auto completion
  echo "source /etc/bash_completion.d/git" >> ~/.bashrc
  echo "source /etc/bash_completion.d/aws_bash_completer" >> ~/.bashrc
  
  # fix python alias and git default editor
  perl -pi -e 's/python27/python36/g' ~/.bashrc
  perl -pi -e 's/nano/vim/g' ~/.bashrc



Ashley's AWS Hacks
------------------

Use at your own risk

  # ashley-aws-hacks
  cd ~/environment/
  git clone https://github.com/ashleygould/ashley-aws-hacks
  cd ./ashley-aws-hacks
  ./shell_setup.sh
  . ~/.bashrc



