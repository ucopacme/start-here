AWS Organizations
==================================

**Context:**
 Document to give an easy to read overview of what an AWS Organization is, and how to create additional OU's and accounts along with Users and Groups.

**Goals:**
 After traversing this document, you should have the initial knowledge needed to create an account within our organizations. 
   


What is an AWS Organization:
-------------------------
- It is an account management services that allows you to consolidate multiple accounts into an Organization that you create and centrally manage them.


What functionality is provided:
-------------------------------
- This allows environemnt to keep track of and structure environments that may be large in size with 'realitive' ease. 
- Consolidated billing for all member accounts
- Hierarchical grouping of your accounts to meet budgetary, security, and compliance needs
- Control over AWS Services
- Intergration and support for IAM



**Walk-thru** Creating AWS Account within an Organization
--------------------------------------------

Files needed to be updated to create new account.
::

/home/djr/.awsorgs/spec.d
[djr@hostname .awsorgs]$ cd spec.d/

[djr@hostname spec.d]$ ls
accounts-specs.yml  custom-policy-spec.yml  groups-spec.yml       orgs-spec.yml  teams-spec.yml
common.yml          delegations-spec.yml    local-users-spec.yml  sc_policy.yml  users-spec.yml

Teams
=====
teams-spec.yml file - team definition file, this file is for ease of understanding who reports to who, what team a person is part of at UCOP. 

- make note of the NAME of the team that best fits the REAL USER.  Note if none of the TEAMS fit, a new team can be added. All fields must be filled out.
::

- Name: operations     <--- make this name meaningful with good.    
    Description: Widget Administrators 
    BusinessContacts:
      - mickey.mouse@company.com
    TechnicalContacts:
      - dumbo@company.com


Users
=====
users-spec.yml file - User definition file. Structure of file is as follows.

The purpose of this file is to CREATE an IAM user in AWS for team members. These IAM users that are created will then be placed into a group (next step).
- The real person you are creatingthis account for, place their information into the file. Required fields are (Name, Email, Team) 
- NOTE: Remember you should of already made note of the team to put this user in from the previous step.

- IMPORTANT NOTE: Indention in field as seen below is very picky. Misallign rows will result in errors.
- Lets add the new team member Scooby Doo to AWS. His username is: sdoo
::

users:
  # 
  - Name: scrappy
    Email: scrappy@company.com
    Team: buildops
  - Name: dopey
    Email: dopey@company.com
    Team: TechSupport
  - Name: sdoo     < --- New user added
    Email: sdoo@company.com  < --- important that the users VALID email is here
    Team: operations   < -- member of team 


Groups
======

groups-spec.yml file - groups definition file. Structure of file is as follows.

- This file is used to place individual IAM users that are created into IAM groups. These trusted IAM groups are than associated with roles needed to manage newly created member accounts. If we just associated IAM users to new member accounts it would be too complex to manage. 
- NOTE: All IAM Users are automatically inherited into the group "UserSelfService" by the definiion of the coding that has been done. This group however only allows IAM users to do such things as (change password, MFA, create keys..)
::

AWS Auth Groups Specification
groups:
  # seg
  - Name: all-users
    Members: ALL
    Policies:
      - UserSelfService
  - Name: admins
    Ensure: present
    Members:
      - dopey
      - scrappy
      - sdoo    < -- Added new user to group (admins)


Delegations
===========

delegations-spec.yml - delegation definition file. Structure of file is as follows.
- This file kind of says what the word says "delegates" what Trusted group can actually do in the newly created member account.
- The glue that ties it all together

- RoleName: Defined in a policy wihin the IAM Group
- TrustingAccount: Target member account(s) the ROLE will be able to assume to.
- TrustedGroup: The IAM group that has IAM user witin it, this group has policies created in it that define Roles which allow a user who is part of that group to Assume a role into another member account.
- RequiredMFA:  ensures it is utilized
- Policies: Service Control Policies as they are called in an organization setup. The services listed and only those services listed are alowed to be used. An explicit allow is used, therefore, all other services are dneied. This is done in a 'whitelisting' of services format. IMPORTANT NOTE: An IAM User or IAM Group that has FULL Administration access are still bound by these policies. The Service Control Policies SUPERCEDES orginal IAM USER and Group permissions.

::


# supers
- RoleName: SuperAdmin
  Ensure: present
  Description:  developer access
  TrustingAccount:
    - goofy-dev
    - pluto-qa
    - mydatacenter
  TrustedGroup: admins
  RequireMFA: True
  Policies:
    - PowerUserAccess
    - LimitedIAM
    - LimitedRoute53
    - ServiceCatalogEndUserFullAccess
    - CascadeServiceUserAccessKeys


Org-spec.yml - Organization location file. Structure file as follows.

- IMPORTANT: Read the descrption at the top of the file.

The following file is basically the 'tree' structure of the Organization. There are parent and child OU's. Beneath both, accounts can be created. Depending on where you define your new account in this file is where it will be created based off the tree structure.

IMPORTANT NOTES TO UNDERSTAND
- If you look at the organizational tree, you will notice that there is a ROOT OU and many CHILD OU's. Notice there is only one account in the ROOT OU, and all others are in a CHILD OU. There can be up to 5 level's of CHILD OU's, but as of now we only go down one level. There can also be N+1 member accounts in any given OU, root or child.

- So to add a new account to the Organization we would modify this file and place the necessary information in the proper location.We are going to add a new account in the child OU (poc-accounts) 

So after we add the account to the proper OU, what exact permission will the account have, what can it do and not do?
- The permissions are exlpicit and filter down from the parent. If we are adding the account "disney-poc" to the OU "poc-accounts". We can see there is no Explicit policies located in its SC_Policies. So what will govern its authority to utilize resources is the PARENT OU? The Parent OU rights filter down to this Child OU.

- In the case of the OU called "build-account". There is an explicit policy on this OU, therefore, this OU can ONLY do what is located within the policy. 

Example of the file is:
::


organizational_units:
  - Name: root
    Accounts:
      -Master
    Child_OU:
      - Name: authentication
        SC_Policies:
          - auth-only
        Accounts:
          - Auth
      - Name: datacenter
        SC_Policies:
        Accounts:
          - mydatacenter
      - Name: poc-accounts
        SC_Policies:
        Accounts:
          - test-poc
          - test1-poc
          - device-poc
          - administrator-poc
          - disney-poc     < -- Added this account to the organization.
      - Name: build-accounts
        SC_Policies:
          - build-account-policy
        Accounts:
          - junkdev
          - hacksville
      - Name: prod
        SC_Policies:
        Accounts:
          - hack-prod



  
Account-specs.yml file - Structure of file. Note read discription at top of file. 

- To add a new account follow the example, reqired fields are (Name, Team, Alias) note reference to Email in decription of file.
::

accounts:
  - Name: widget
    Team: operations
    Alias: widgetops
    Email: wo@company.com
  - Name: mydatacenter  < --- We are adding this new account
    Team: operations    < -- what team is using this account
    Alias: datacenter01 < -- the alias for the new account. you can use this alias to assume role
    Email:awsaccount@company.com  < -- Although this email address really does not matter, it must be 100% unique within AWS.



Creating Member Accounts
========================

All the above information is kind of housekeeping and an informal introduction into what is needed to create a new account.

- The mechanism used to create new member accounts within the Organization is the 'AWS-ORGS' toolset.

- In order to create a fully functioning account within an Organization than the following information is needed that was fully covered above.

Required info:
(update or gather information from the following files)
1. users-spec.yml
2. groups-spec.yml
3. teams-spec.yml
4. orgs-spec.yml
5. accounts-specs.yml
6. delegations-spec.yml

These commands will create the new member account based off the information you have supplied in the files lsted above in "Required info"
::

# Create Account


$ awsaccounts create --config /home/djr/.awsorgs/config.yaml --spec-dir /home/djr/.awsorgs/spec.d --master-account-id "222222222222" --auth-account-id "3333333333333" --org-access-role SuperAdmin    < -- dryrun only


$ awsaccounts create --config /home/djr/.awsorgs/config.yaml --spec-dir /home/djr/.awsorgs/spec.d --master-account-id "222222222222" --auth-account-id "3333333333333" --org-access-role SuperAdmin    < --  execute command


# Delegation 
$ awsauth delegations  < --  dryrun only
$ awsauth delegations --exec   < -- execute command 


# LoginProfile for users created
$ awsloginprofile --new sdoo   < --- dry run only
$ awsloginprofile --new sdoo --exec    < -- execute command

#OOOPS I messed up on the person email address in the 'users-spec.yml'

# will rerun and update loginprofile

$ awsloginprofile --update sdoo   < --- dry run only
$ awsloginprofile --update sdoo --exec    < -- execute command


You should of received an email with the steps needed to complete the process and login to your new account!!!
