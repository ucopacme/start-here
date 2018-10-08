import re
from moto import mock_sns
from boto3_create_sns_topic import (
    create_sns_topic,
    get_topic_arn,
    delete_sns_topic
)


TOPIC_NAME = 'test_topic'
ACCOUNT_ID_REGEX = r'[0-9]{12}'
ARN_REGEX = re.compile(r'arn:aws:sns:\w+\-\w+\-\d:\d{12}:%s' % TOPIC_NAME)


@mock_sns
def test_create_sns_topic():
    topic_arn =  create_sns_topic(TOPIC_NAME)
    #print(topic_arn)
    assert isinstance(topic_arn, str)
    assert ARN_REGEX.match(topic_arn)


@mock_sns
def test_get_topic_arn():
    create_sns_topic(TOPIC_NAME)
    topic_arn =  get_topic_arn(TOPIC_NAME)
    assert isinstance(topic_arn, str)
    assert ARN_REGEX.match(topic_arn)


@mock_sns
def test_delete_sns_topic():
    create_sns_topic(TOPIC_NAME)
    delete_sns_topic(TOPIC_NAME)
    topic_arn =  get_topic_arn(TOPIC_NAME)
    assert topic_arn is None


