#!/bin/env python 
import sys
import boto3 


REGION = 'us-west-2'
IMAGE_ID = 'ami-6cd6f714'
INSTANCE_TYPE = 't1.micro'
SECURITY_GROUP = 'sg-0e19a5c91255a49ba'
SSHKEY = 'ashley@isis'


#ec2 = boto3.resource('ec2', REGION, aws_access_key_id="", aws_secret_access_key="")

def usage():
    print(sys.argv[0])

def make_instance():
    ec2= boto3.resource('ec2', region_name=REGION )
    instance = ec2.create_instances(
        ImageId=IMAGE_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
    )
    return instance[0].id

def list_instances():
    ec2 = boto3.resource('ec2',region_name='us-west-2' )
    for instance in ec2.instances.all():
        print (instance.id, instance.state) 
        
def terminate_instances(termID):
    ec2 = boto3.resource('ec2',region_name='us-west-2' )
    instanceTerm = ec2.Instance(termID)
    response = instanceTerm.terminate() 
    #print (response)
                
if __name__ == '__main__':

    if len(sys.argv) > 1:
        action = sys.argv[1]
    else:
        sys.exit(usage())

    if action == 'create':
        instance_id = make_instance()
        print(instance_id)
    elif action == 'report':
        list_instances()
    elif action == 'delete':
        terminate_instances()
    else:
        sys.exit(usage())
