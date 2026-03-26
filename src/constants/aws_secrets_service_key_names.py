
class AwsSecretsServiceKeyNames:

    @classmethod
    def get_mongo_connection_string_name(cls, env_name: str) -> str:
        return f"be_lambda_{env_name}_mongodb_connection_string"

    @classmethod
    def get_aws_access_key_id_name(cls, env_name: str) -> str:
        return f"{env_name}_service_aws_access_key_id"

    @classmethod
    def get_aws_secret_access_key_name(cls, env_name: str) -> str:
        return f"{env_name}_service_aws_secret_access_key"

    @classmethod
    def get_api_deck_api_key_name(cls, env_name: str) -> str:
        return f"{env_name}_api_deck_api_key"

    @classmethod
    def get_api_deck_app_id_name(cls, env_name: str) -> str:
        return f"{env_name}_api_deck_app_id"

