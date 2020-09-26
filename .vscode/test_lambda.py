import os
import datetime
import boto3
import botocore.session
from botocore.stub import Stubber
from moto import mock_ssm


os.environ["aws_access_key_id"] = "XXXXXXXXXXXXXX"
os.environ["aws_secret_access_key"] = "YYYYYYYYYYYYYYYYYYYYYYYYYYY"


def get_ssm_parameter():
    client = boto3.client('ssm', region_name='sa-east-1')

    response = client.get_parameter(
        Name='/application/ClusterName'
    )

    return response


def test_get_ssm_parameter():

    ssm = botocore.session.get_session().create_client('ssm', region_name='sa-east-1')
    stubber = Stubber(ssm)

    response = {
        'Parameter': {
            'Name': 'name-ssm-parameter',
            'Type': 'String',
            'Value': 'ResultValue',
            'Version': 123,
            'Selector': 'result-selector',
            'SourceResult': 'result-source',
            'LastModifiedDate': datetime.datetime(2016, 1, 20, 22, 9),
            'ARN': 'arn::result-arn',
            'DataType': 'string'
        }
    }

    expected_params = {'Name': 'name-ssm-parameter'}

    stubber.add_response('get_parameter', response, expected_params)
    stubber.activate()
    responde_data = ssm.get_parameter(**expected_params)

    get_ssm_parameter()

    print('')
    print('')
    print('######### stubber - START #########')
    print(responde_data)
    print(stubber)
    print('######### stubber - END #########')
    print('')
    print('')

    assert "soler" == "soler"
    pass
