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
#Create s3 Bucket
     s3 = boto3.client('s3')
     response =  s3.create_bucket(Bucket=new_buck, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
     print(response)
     return response
 

def dels3(new_buck):
#Delete s3 Bucket
      s3 = boto3.client('s3')
      delbuck = s3.delete_bucket(Bucket=new_buck)
      print(delbuck)
      return delbuck

def main():
    mybuck = 'lab1davidpythons3'
    result = creates3(mybuck)
    print('S3 Bucket being created')
    print('----------------------------')
    print(yamlfmt(result['Location']))

    mybuck = 'lab1davidpythons3'
    result = dels3(mybuck)
    print(' Delete S3 Bucket')
    print('---------------------')
    



if __name__ == "__main__":
    main()
