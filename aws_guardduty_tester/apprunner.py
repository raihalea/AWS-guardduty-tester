from aws_cdk import (
    Stack,
    aws_ecr_assets as assets,
    aws_apprunner_alpha as apprunner
)
from constructs import Construct
import boto3


class AppRunnerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecr_asset = assets.DockerImageAsset(self,
            "tester",
            directory= "./tester"
        )

        service = apprunner.Service(
            self,
            "Service",
            source=apprunner.Source.from_asset(
                image_configuration=apprunner.ImageConfiguration(port=80),
                asset=ecr_asset
            )
        )