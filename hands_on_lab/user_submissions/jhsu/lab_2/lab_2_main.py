#! /usr/bin/env python

import time
import boto3
import json
import yaml

import myutil as util
import lab_2_def as iam

if __name__ == "__main__":

   iam_client   = boto3.client('iam')

   User1 = 'John'
   User2 = 'Michael'

   print("--- IAM list users: ---")
   (iam_user_list, iam_user_cnt) = iam.iam_list_users(iam_client)
   util.iam_print_user_list(iam_user_list)
 
   print("--- IAM create user:", User1, "---")
   iam_create_user_response  = iam.iam_create_user(iam_client, User1)

   print("--- Validate user creation ---")
   if iam.iam_check_user_in_list(iam_client, User1):
      print(" User creation passed! ")
   else:
      print(" User creation failed! ")

   print("--- IAM list users: ---")
   (iam_user_list, iam_user_cnt) = iam.iam_list_users(iam_client)
   util.iam_print_user_list(iam_user_list)
 
   print("--- IAM create user:", User2, "---")
   iam_create_user_response  = iam.iam_create_user(iam_client, User2)

   print("--- Validate user creation ---")
   if iam.iam_check_user_in_list(iam_client, User2):
      print(" User creation passed! ")
   else:
      print(" User creation failed! ")

   print("--- IAM list users: ---")
   (iam_user_list, iam_user_cnt) = iam.iam_list_users(iam_client)
   util.iam_print_user_list(iam_user_list)
 
   print("--- IAM delete user: ---")
   iam.iam_delete_user(iam_client, User1)
   print("--- IAM delete user: ---")
   iam.iam_delete_user(iam_client, User2)

   print("--- IAM list users: ---")
   (iam_user_list, iam_user_cnt) = iam.iam_list_users(iam_client)
   util.iam_print_user_list(iam_user_list)
 

