#!/home/drivera/python/python36/bin/python3

import boto3

s3 = boto3.client('s3')

def creates3():
 #Create s3 Bucket
 s3bucket =  s3.create_bucket(Bucket='lab1davidpython', CreateBucketConfiguration={
	'LocationConstraint': 'us-west-2'})
 print('')
 print('S3 Bucket being created')
 print('----------------------------')
 print(s3bucket)
creates3()

def listbucket():
  response = s3.list_buckets()
  buckets = [bucket['Name'] for bucket in response['Buckets']]

listbucket()
# Upload file from CWD to the new s3 bucket

def uploadfile():
 
 filexfer =  s3.upload_file('lab1daviddoc.txt', 'lab1davidpython', 'remotefile.txt')
# print(filexfer) 
uploadfile()
# 

def lists3obj():
  response = s3.list_objects(
      Bucket='lab1davidpython'
	  )
  print()
  print()
#  print("s3 Bucket Name: %s" % response.get('Name'))
  print()
  print()
  print(' Data Transfered to S3 Bucket')
  print('-----------------------------------------------')
  print("Makeup of s3 Bucket: %s" % response.get('Contents'))
lists3obj()
def dels3():  
  s3 = boto3.resource('s3')
  b = s3.Bucket('lab1davidpython')
  b.objects.filter(Prefix='remotefile.txt').delete()
  s3 = boto3.client('s3')
  delbuck = s3.delete_bucket(
  Bucket='lab1davidpython'
   )
  print()
  print()
  print(' Delete S3 Bucket')
  print('---------------------')
  print(delbuck)
dels3()
