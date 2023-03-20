from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

from .base_stack import BaseStack
from .ec2_stack import Ec2Stack


class AwsGuarddutyTesterStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        base = BaseStack(self, "AwsGuarddutyTesterBaseStack")

        # EC2
        ec2 = Ec2Stack(self, "AwsGuarddutyTesterEc2Stack", base)
        ec2.add_dependency(base)