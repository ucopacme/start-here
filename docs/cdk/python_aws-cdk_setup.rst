Python AWS-CDK Environment Setup
================================


nvm
***

::

  nvm current
  nvm ls-remote | tail
  nvm install stable
  nvm install --latest-npm
  nvm use stable
  nvm current

cdk
***

::

  which cdk
  npm install -g aws-cdk
  npm update -g aws-cdk
  cdk --version

python
******

::

  cdk init -l python
  rm -rf .env
  python3 -m venv .env
  pip install -r requirements.txt


