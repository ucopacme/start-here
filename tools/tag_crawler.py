#!/usr/bin/env python
'''
TagFilters=[
    {
        'Key': 'string',
        'Values': [
            'string',
        ]
    },
],
ResourceTypeFilters=[
    'string',
]
'''


import boto3
from organizer import crawlers, orgs, utils


def get_tags(region, account):
    client = boto3.client(
        'resourcegroupstaggingapi', 
        region_name=region, 
        **account.credentials,
    )
    filters = dict(
        TagFilters=[
            #dict(Key='Name'),
            #dict(Key='24hourssh'),
            #dict(Key='aws:cloudformation:stack-name'),
        ],
        ResourceTypeFilters=['ec2:instance'],
    )
    response = client.get_resources(
        #**filters,
    )
    tag_mapping_list = response['ResourceTagMappingList']
    while response['PaginationToken']:
        response = client.get_resources(
            #**filters,
            PaginationToken=response['PaginationToken'],
        )
        tag_mapping_list += response['ResourceTagMappingList']
    return dict(ResourceTagMappingList=tag_mapping_list)


def get_crawler(org_access_role):
    master_account_id = utils.get_master_account_id(org_access_role)
    my_org = orgs.Org(master_account_id, org_access_role)
    my_org.load()
    my_crawler = crawlers.Crawler(
        my_org,
        access_role=org_access_role,
        #accounts=test_accounts,
        accounts=['ait-poc', 'ashley-training'],
        regions=['us-west-2', 'us-east-1'],
    )
    my_crawler.load_account_credentials()
    return my_crawler


def output_regions_per_account(execution):
    """ generate dictionary of responses per account """
    # purge empty responses
    responses = [
        r for r in execution.responses 
        if r.payload_output['ResourceTagMappingList']
    ]
    # list of account names unique and sorted
    account_names = sorted(list(set([r.account.name for r in responses])))
    collector = []
    for account_name in account_names:
        d = dict(
            Account=account_name,
            Regions=[{r.region: r.payload_output}
                for r in responses
                if r.account.name == account_name
            ]
        )
        collector.append(d)
    return(utils.yamlfmt(collector))


def main():
    org_access_role = 'awsauth/OrgAdmin'
    crawler = get_crawler(org_access_role)
    execution = crawler.execute(get_tags)
    output = output_regions_per_account(execution)
    print(output)


if __name__ == "__main__":
    main()
