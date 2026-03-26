import os
import pathlib
from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import SettingsConfigDict, BaseSettings

from src.config.secrets_manager_service import AWSSecretsManagerService
from src.constants.aws_secrets_service_key_names import AwsSecretsServiceKeyNames
from src.enums.env_enum import Env

STAGING_CONFIG_FILE = str(pathlib.Path().joinpath('src/.staging.env'))
PRODUCTION_CONFIG_FILE = str(pathlib.Path().joinpath('src/.production.env'))


class AppConfig(BaseSettings):
    port: int
    env_name: Env
    # cognito_user_pool_id: str
    # aws_access_key_id: str = None
    # aws_secret_access_key: str = None
    #
    # outlook_client_id: str = None
    # outlook_client_secret: str = None

    model_config = SettingsConfigDict(
        env_file=PRODUCTION_CONFIG_FILE if os.getenv('ENV_NAME') == 'prod' else STAGING_CONFIG_FILE,
        extra='ignore'  # Allow extra fields in env file
    )
    #
    # @field_validator('aws_access_key_id', mode='before')
    # def _set_aws_access_key_id(cls, v, values):
    #     return AWSSecretsManagerService.get_secret(
    #         AwsSecretsServiceKeyNames.get_aws_access_key_id_name(values['env_name'].value)
    #     )
    #
    # @field_validator('aws_secret_access_key', mode='before')
    # def _set_aws_secret_access_key(cls, v, values):
    #     return AWSSecretsManagerService.get_secret(
    #         AwsSecretsServiceKeyNames.get_aws_secret_access_key_name(values['env_name'].value)
    #     )
    #
    # @field_validator('outlook_client_id', mode='before')
    # def _set_ms_outlook_app_client_id(cls, v, values):
    #     return AWSSecretsManagerService.get_secret(
    #         AwsSecretsServiceKeyNames.get_ms_outlook_app_client_id_key_name()
    #     )


@lru_cache
def get_configs():
    return AppConfig()
