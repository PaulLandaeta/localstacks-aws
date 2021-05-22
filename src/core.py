import json
import boto3
import botocore

CONFIG = botocore.config.Config(retries={'max_attempts': 0})
def get_lambda_client():
    return boto3.client(
        'lambda',
        region_name='us-east-1',
        endpoint_url='http://localhost:4566',
        config=CONFIG
    )


def invoke_function_and_get_message(function_name):
    lambda_client = get_lambda_client()
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'
    )
    return json.loads(
        response['Payload']
        .read()
        .decode('utf-8')
    )

def run():
    print(invoke_function_and_get_message('test'))

if __name__ == '__main__':
    run()
