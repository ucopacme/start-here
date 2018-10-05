#!/bin/env python 
import sys
import boto3 


IMAGE_ID = 'ami-6cd6f714'
INSTANCE_TYPE = 't1.micro'
SECURITY_GROUP = 'sg-0e19a5c91255a49ba'
SSHKEY = 'ashley@isis'


def usage():
    print(sys.argv[0])

def launch_instance(dryrun=False):
    ec2_client = boto3.client('ec2')
    response = ec2_client.run_instances(
        ImageId=IMAGE_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        KeyName=SSHKEY,
        SecurityGroupIds=[SECURITY_GROUP],
        DryRun=dryrun,
    )
    return response


def list_my_instances():
    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances(
        Filters=[
            dict(Name='key-name',Values=[SSHKEY]),
            dict(Name='image-id',Values=[IMAGE_ID]),
            dict(Name='instance-type',Values=[INSTANCE_TYPE]),
        ]
    )
    list = []
    for instance in [r['Instances'][0] for r in response['Reservations']]:
        if instance['State']['Name'] != 'terminated':
            pub_ip = instance['PublicIpAddress']
        else:
            pub_ip = None
        list.append(dict(
            InstanceId=instance['InstanceId'], 
            PublicIpAddress=pub_ip,
            State=instance['State']['Name'],
        ))
    return list

        
def terminate_my_instances(dryrun=False):
    ec2_client = boto3.client('ec2')
    for instance_id in [i['InstanceId'] for i in list_my_instances()]:
        print('terminating instance id: {}'.format(instance_id))
        ec2_client.terminate_instances(InstanceIds=[instance_id], DryRun=dryrun)

                
if __name__ == '__main__':

    if len(sys.argv) > 1:
        action = sys.argv[1]
    else:
        sys.exit(usage())

    if action == 'create':
        instance_id = launch_instance()
        print(instance_id)

    elif action == 'report':
        for instance in list_my_instances():
            print(instance)

    elif action == 'delete':
        terminate_my_instances()

    else:
        sys.exit(usage())
