from functools import lru_cache
from logging import getLogger

from boto3.session import Session
from botocore.exceptions import ClientError

logger = getLogger(__name__)


class AWSSecretsManagerService:

    @staticmethod
    @lru_cache(maxsize=128)
    def get_secret(secret_name, aws_region='us-east-1'):
        session = Session()
        client = session.client(
            service_name="secretsmanager",
            region_name=aws_region
        )
        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as E:
            logger.error(
                f"Error occurred while trying to get secret: {secret_name} from AWS Secrets Manager. Error: {E}")
            raise E
        else:
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
            else:
                from base64 import b64decode
                secret = b64decode(get_secret_value_response['SecretBinary'])
            logger.info(f"Secret retrieved from AWS Secrets Manager {secret_name}")
            return secret
