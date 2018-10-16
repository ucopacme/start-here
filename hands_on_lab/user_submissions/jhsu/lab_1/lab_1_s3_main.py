#! /home/jhsu/python/python3/bin/python3

import time
import boto3
import json
import yaml

import lab_1_s3_def as s3

def main():
   s3_resource = boto3.resource('s3')
   s3_client   = boto3.client('s3')

   print( 2 * '\n')
   print('s3_clent object:')
   print(s3_client)
   print()

   test_bucket= 'jhsu-s3-boto3-bucket1'
   test_file  = 'jhsu-s3-boto3-file1'
  

   s3_bucket_list = []
   s3.s3_list_buckets(s3_client)

   print()
   s3_bucket_url = s3.s3_create_bucket(s3_client, test_bucket)
   print(s3_bucket_url)
   print()
   (s3_bucket_list, s3_bucket_count) = s3_bucket_list = s3.s3_list_buckets(s3_client)

   print()
   s3_bucket_deleted = s3.s3_delete_bucket(s3_client, test_bucket)
   print(type(s3_bucket_deleted))
   print()
   s3.s3_list_buckets(s3_client)
   print()

   return

main()
