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

import click
import boto3
from organizer import crawlers, orgs, utils


def parse_tags(tag_tuple):
    tag_filter = []
    for tag in tag_tuple:
        key, sep, value = tag.partition(',')
        if value:
            tag_filter.append(dict(Key=key, Values=[value]))
        else:
            tag_filter.append(dict(Key=key))
    return tag_filter


def parse_filters(tag_tuple, resource_tuple):
    filters = dict()
    if tag_tuple is not None:
        filters['TagFilters'] = parse_tags(tag_tuple)
    if resource_tuple is not None:
        filters['ResourceTypeFilters'] = list(resource_tuple)
    return filters

    #filters = dict(
    #    TagFilters=[
    #        dict(Key='Name'),
    #        #dict(Key='24hourssh'),
    #        #dict(Key='aws:cloudformation:stack-name'),
    #    ],
    #    ResourceTypeFilters=['ec2:instance'],
    #)

def get_tagged_resources(region, account, filters):
    """
    orgcrawler payload function
    """
    client = boto3.client(
        'resourcegroupstaggingapi', 
        region_name=region, 
        **account.credentials,
    )
    response = client.get_resources(
        **filters,
    )
    tag_mapping_list = response['ResourceTagMappingList']
    while response['PaginationToken']:
        response = client.get_resources(
            **filters,
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
        accounts=['ait-poc', 'ashley-training'],
        regions=['us-west-2', 'us-east-1'],
    )
    my_crawler.load_account_credentials()
    return my_crawler


def purge_empty_responses(execution):
    '''
    Return list of execution responses for which output is not empty.
    Expects each response to be a list of dict.
    '''
    responses = [
        r for r in execution.responses 
        if len(r.payload_output) == 1
        and list() not in r.payload_output.values()
    ]
    return responses


def output_regions_per_account(execution):
    """ generate dictionary of responses per account """
    collector = []
    responses = purge_empty_responses(execution)
    account_names = sorted(list(set([r.account.name for r in responses])))
    for account_name in account_names:
        d = dict(
            Account=account_name,
            Regions=[{r.region: r.payload_output}
                for r in responses
                if r.account.name == account_name
            ]
        )
        collector.append(d)
    return(collector)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--role', '-r', required=True,
    help='IAM role for accessing AWS Organization accounts')
@click.option('--tag', multiple=True, type=str,
    help='Tag to filter by. Can be used multiple times. Must be a string. Can be either a key name or a key/value pair saparated by a comma. Tags containing spaces must be quoted.')
@click.option('--resource', multiple=True, type=str,
    help='AWS resource name to filter by. Can be used multiple times.')
def main(role, tag, resource):
    #click.echo(tag)
    #click.echo(resource)
    #tag_filter = parse_tags(tag)
    #click.echo(utils.yamlfmt(tag_filter))
    filters = parse_filters(tag, resource)
    #click.echo(utils.yamlfmt(filters))
    crawler = get_crawler(role)
    execution = crawler.execute(get_tagged_resources, filters)
    output = output_regions_per_account(execution)
    click.echo(utils.yamlfmt(output))


if __name__ == "__main__":
    main()
