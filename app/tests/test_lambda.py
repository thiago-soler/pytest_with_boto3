import datetime
import boto3
from moto import mock_ssm
from app.lambda_function import get_ssm_parameter


@mock_ssm
def test_get_ssm_param():
    ssm = boto3.client('ssm', region_name='sa-east-1')
    ssm.put_parameter(
        Name="/application/ClusterName",
        Description="Mock ssm parameter",
        Value="The value of parameter",
        Type="String",
    )

    parameter_data = get_ssm_parameter().get('Parameter', {})

    assert parameter_data.get('Name') == "/application/ClusterName"
    assert parameter_data.get('Value') == "The value of parameter"
