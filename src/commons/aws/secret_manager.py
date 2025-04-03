import json
import boto3
from botocore.exceptions import ClientError

def get_cfm_access_key(secret_name: str, region: str) -> str:
    print("Getting CFM access key secret.")
    access_key = None
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key = secret['CFM_ACCESS_KEY'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()

def get_slack_webhook(secret_name: str, region: str) -> str:
    print("Getting Webhook access key secret.")
    access_key = None
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key = secret['URL'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()

def get_sharepoint_access_key(secret_name: str, region: str) -> dict:
    print("Getting Sharepoint access key secret.")
    access_key = {}
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key['username'] = secret['username'].strip()
        access_key['password'] = secret['password'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()    

def get_infosimples_access_key(secret_name: str, region: str) -> dict:
    print("Getting InfoSimples access key secret.")
    access_key = None
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key = secret['infosimples_token'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()

def get_google_console_access_key(secret_name: str, region: str) -> dict:
    print("Getting Google Console access key secret.")
    access_key = {}
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        return secret
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()


def get_braze_api_params(secret_name: str, region: str) -> dict:
    print("Getting Braze Api Params secret.")
    
    access_key = {}
    client = None
    try:
        
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key['api_key'] = secret['api_key'].strip()
        access_key['rest_api_url'] = secret['rest_api_url'].strip()
        access_key['segment_id'] = secret['segment_id'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()


def get_s3_peb_params(secret_name: str, region: str) -> dict:
    print("Getting S3 Peb Params secret.")
    access_key = {}
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key['AWS_ACCESS_KEY'] = secret['AWS_ACCESS_KEY'].strip()
        access_key['AWS_SECRETS_KEY'] = secret['AWS_SECRETS_KEY'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()

def get_hubspot_access_key(secret_name: str, region: str) -> dict:
    print("Getting Hubspot access key secret.")
    access_key = None
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        access_key = secret['oauth_token'].strip()
        return access_key
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()

## GENERICO
def get_secret_key(secret_name: str, region: str) -> dict:
    
    access_key = None
    client = None
    try:
        client = boto3.client(service_name='secretsmanager', region_name=region)
        get_secret_value_response = client.get_secret_value( SecretId=secret_name )
        secret = json.loads(get_secret_value_response['SecretString'].strip())
        return secret
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise e
    finally:
        if client:
            client.close()