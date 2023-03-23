from aws_cdk import (
    Stack,
)
from constructs import Construct

from .base_stack import BaseStack
from .ec2_stack import Ec2Stack
from .ecs_ec2_stack import EcsEc2Stack
from .ecs_fargate_stack import EcsFargateStack
from .eks_ec2_stack import EksEc2Stack
from .eks_fargate_stack import EksFargateStack
from .cloud9 import Cloud9Stack
from .apprunner import AppRunnerStack
from .lambda_ import LambdaStack
from .lambda_vpc import LambdaVpcStack
from .lightsail import LightsailStack
from .batch_ec2 import BatchEc2Stack


class AwsGuarddutyTesterStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        base = BaseStack(self, "AwsGuarddutyTesterBaseStack")

        # EC2
        ec2 = Ec2Stack(self, "AwsGuarddutyTesterEc2Stack", base)
        ec2.add_dependency(base)

        # ECS EC2
        ecs_ec2 = EcsEc2Stack(self, "AwsGuarddutyTesterEcsEc2Stack", base)
        ecs_ec2.add_dependency(base)

        # ECS Fargate
        ecs_fargate = EcsFargateStack(self, "AwsGuarddutyTesterEcsFargateStack", base)
        ecs_fargate.add_dependency(base)

        # EKS EC2
        eks_ec2 = EksEc2Stack(self, "AwsGuarddutyTesterEKsEc2Stack", base)
        eks_ec2.add_dependency(base)

        # EKS Fargate
        eks_fargate = EksFargateStack(self, "AwsGuarddutyTesterEKsFargateStack", base)
        eks_fargate.add_dependency(base)

        # Cloud9
        # dig guarddutyc2activityb.com
        cloud9 = Cloud9Stack(self, "AwsGuarddutyTesterCloud9Stack", base)
        eks_fargate.add_dependency(base)

        # AppRunner
        apprunenr = AppRunnerStack(self, "AwsGuarddutyTesterAppRunnerStack")

        # Lambda
        lambda_ = LambdaStack(self, "AwsGuarddutyTesterLambdaStack")

        # Lambda VPC
        lambda_vpc = LambdaVpcStack(self, "AwsGuarddutyTesterLambdaVpcStack", base)
        lambda_vpc.add_dependency(base)

        # Lightsail
        lightsail = LightsailStack(self, "AwsGuarddutyTesterLightsailStack")

        # Batch EC2
        batch_ec2 = BatchEc2Stack(self, "AwsGuarddutyTesterBatchEC2Stack", base)
        batch_ec2.add_dependency(base)