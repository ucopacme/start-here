#! /home/jhsu/python/py3/bin/python3

import time
import boto3
import json
import yaml

import lab_2_def as iam

if __name__ == "__main__":

    iam_client   = boto3.client('iam')

    User1 = 'John'
    User2 = 'Michael'

    print("--- IAM list users: ---")
    iam_list_users_response = iam.iam_list_users(iam_client)
 
    print("--- IAM create user:", User1, "---")
    iam_create_user_response  = iam.iam_create_user(iam_client, User1)

    print("--- IAM list users: ---")
    iam_list_users_response = iam.iam_list_users(iam_client)
 
    print("--- IAM create user:", User2, "---")
    iam_create_user_response  = iam.iam_create_user(iam_client, User2)

    print("--- IAM list users: ---")
    iam_list_users_response = iam.iam_list_users(iam_client)
 
    print("--- IAM delete user: ---")
    iam.iam_delete_user(iam_client, User1)
    print("--- IAM delete user: ---")
    iam.iam_delete_user(iam_client, User2)

    print("--- IAM list users: ---")
    iam_list_users_response = iam.iam_list_users(iam_client)
 

