from aws_cdk import (
    Stack,
    aws_ecs as ecs,
)
from constructs import Construct


class EcsFargateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cluster = ecs.Cluster(self, "Cluster", vpc=base.vpc)

        task_definistion = ecs.FargateTaskDefinition(
            self,
            "TaskDef",
        )
        task_definistion.add_container(
            "tester",
            image=ecs.ContainerImage.from_asset("./tester/"),
            logging=ecs.AwsLogDriver(stream_prefix="tester-fargate"),
        )

        service = ecs.FargateService(
            self, "Service", cluster=cluster, task_definition=task_definistion
        )
