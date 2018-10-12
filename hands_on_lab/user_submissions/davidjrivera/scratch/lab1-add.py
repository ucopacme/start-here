#!/home/drivera/python/python36/bin/python3

import boto3
# Create s3 Bucket
s3 = boto3.client('s3')
s3.create_bucket(Bucket='lab1davidpython', CreateBucketConfiguration={
	'LocationConstraint': 'us-west-2'})

response = s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Upload file from CWD to the new s3 bucket
s3.upload_file('lab1daviddoc.txt', 'lab1davidpython', 'remotefile.txt')

# 
response = s3.list_objects(
    Bucket='lab1davidpython'
	)

print()
print()
print("s3 Bucket Name: %s" % response.get('Name'))
print()
print()
print("Makeup of s3 Bucket: %s" % response.get('Contents'))
s3 = boto3.resource('s3')
b = s3.Bucket('lab1davidpython')
b.objects.filter(Prefix='remotefile.txt').delete()
print("Bucket List: %s" % buckets)
s3 = boto3.client('s3')
response = s3.delete_bucket(
   Bucket='lab1davidpython'
)
