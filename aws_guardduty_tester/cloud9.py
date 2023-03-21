from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_cloud9 as cloud9,
)
from constructs import Construct
import boto3


class Cloud9Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        sts = boto3.client("sts")
        whoami = sts.get_caller_identity().get("Arn")

        cloud9_instance = cloud9.CfnEnvironmentEC2(
            self,
            "Cloud9Env",
            instance_type="t2.micro",
            subnet_id=base.vpc.select_subnets(
                subnet_type=ec2.SubnetType.PUBLIC
            ).subnet_ids[0],
            owner_arn=whoami,
        )
