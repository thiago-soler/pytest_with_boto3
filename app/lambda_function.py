import boto3
import pytest


def get_ssm_parameter():
    client = boto3.client('ssm', region_name='sa-east-1')

    response = client.get_parameter(
        Name='/application/ClusterName'
    )

    return response
