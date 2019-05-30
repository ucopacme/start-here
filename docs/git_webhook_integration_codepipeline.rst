Process to Create GitHub Pipeline with AWS Cloudformation
=========================================================

AWS Codepipeline can be triggered whenever new code changes are pushed into GitHub using change-dectection resource(GitHub Webhooks)

To Setup this, there are some pre-requisites needed. 

- Create a OAuth Token for your account
- Create a GitHub repository and branch to be used. 
- Have the GitHub Owner name ready(Organization name)

Any Pipeline with GitHub will have atleast 2 stages of which the stage would be GitHub Source stage



Creating a OAuth token:

- Login to your GitHub account
- Click on 'settings' on your profile
- On the left hand menu, go to 'Developer settings'
- Select 'Personal Access Token' and Click 'Generate new token' button
- Be specific and Select only the access required(Preferably Read access only).
- Generate token and save this token as it is shown only this one time. 


Next, the cloudformation template to create the codepipeline should have the following details:
------------------------------------------------------------------------------------------------


In Parameters section should be added with the following:: 

  ProjectRepository:
    Type: String
    Description: Name of github repo for project
  ProjectBranch:
    Type: String
    Description: The branch of the project repository this pipeline will monitor
    Default: master
  GitHubOwner:
    Type: String
  GitHubSecret:
    Type: String
    NoEcho: true
  GitHubOAuthToken:
    Type: String
    NoEcho: true


And these parameters are provided while building the stack. 



A GitHub webhook needs to be created in the template, and through the webhook the codepipeline will be monitoring the specified branch

Template for GitHub webhook::

   DocBuilderPipelineWebhook:
    Type: 'AWS::CodePipeline::Webhook'
    Properties:
      Authentication: GITHUB_HMAC
      AuthenticationConfiguration:
        SecretToken: !Ref GitHubSecret
      Filters:
        - JsonPath: $.ref
          MatchEquals: 'refs/heads/{Branch}'
      TargetPipeline: !Ref DocBuilderPipeline
      TargetAction: SourceAction       # Action name should match source action name in the Pipeline stage
      Name: DocBuilderPipelineWebhook
      TargetPipelineVersion: !GetAtt
        - DocBuilderPipeline
        - Version
      RegisterWithThirdParty: true


Source stage step in the Pipeline::

  Stages:
        - Name: Source
          Actions:
            - Name: SourceAction
              ActionTypeId:
                Category: Source
                Owner: ThirdParty
                Provider: GitHub
                Version: 1
              Configuration:
                Owner: !Ref GitHubOwner
                Branch: !Ref ProjectBranch
                OAuthToken: !Ref GitHubOAuthToken
                Repo: !Ref ProjectRepository
                PollForSourceChanges: false
              OutputArtifacts:
                - Name: ProjectSource
              RunOrder: '1'


When the cloudformation stack is created, provide GitHub owner, a secret token(not GitHub password), OAuth Token, branch
and your pipeline is ready with GitHub integration.  

