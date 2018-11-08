#!/bin/env python

#
# Usage: ./lab1-add-01.py
#

import boto3
import yaml


def yamlfmt(obj):
    if isinstance(obj, str):
        return obj
    return yaml.dump(obj, default_flow_style=False)

def creates3(new_buck):
     s3 = boto3.client('s3')
     response =  s3.create_bucket(Bucket=new_buck, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
     #print(response['Location'])
     return response
 

def dels3(new_buck):
      s3 = boto3.client('s3')
      delbuck = s3.delete_bucket(Bucket=new_buck)
      listbuck = s3.list_buckets()
      #print(listbuck['Name'])
      return delbuck

def main():
    new_buck = 'lab1davidpythons3'
    create_result = creates3(new_buck)
    print()
    print('S3 Bucket being created')
    print('----------------------------')
    print(yamlfmt(create_result['Location']))
    print()

    mybuck = 'lab1davidpythons3'
    result = dels3(mybuck)
    print(' Delete S3 Bucket')
    print('---------------------')
    



if __name__ == "__main__":
    main()
