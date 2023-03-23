from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_batch_alpha as batch,
    aws_ecs as ecs
)
from constructs import Construct


class BatchEc2Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        batch_ce = []

        batch_environment = batch.ComputeEnvironment(
            self, "Batch", compute_resources=batch.ComputeResources(vpc=base.vpc)
        )

        batch_ce.append(
            batch.JobQueueComputeEnvironment(
                compute_environment=batch_environment, order=1
            )
        )

        self.batche_queue = batch.JobQueue(self, "JobQueue", compute_environments=batch_ce)

        batch_jofDef = batch.JobDefinition(
            self,
            "jobDef",
            container=batch.JobDefinitionContainer(
                image=ecs.ContainerImage.from_asset("./tester/"),
                command=["dig", "guarddutyc2activityb.com"],
                memory_limit_mib=6,
                log_configuration=batch.LogConfiguration(
                    log_driver=batch.LogDriver.AWSLOGS
                )
            )
        )
