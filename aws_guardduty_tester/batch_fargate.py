from aws_cdk import (
    Stack,
    aws_batch_alpha as batch,
    aws_ecs as ecs,
    aws_iam as iam,
)
from constructs import Construct


class BatchFargateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        batche_queue = batch.JobQueue(
            self,
            "JobQueue",
            compute_environments=[
                batch.JobQueueComputeEnvironment(
                    compute_environment=batch.ComputeEnvironment(
                        self,
                        "Batch",
                        compute_resources=batch.ComputeResources(
                            vpc=base.vpc, type=batch.ComputeResourceType.FARGATE
                        ),
                    ),
                    order=1,
                )
            ],
        )

        task_execution_role = iam.Role(
            self,
            "TaskExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonECSTaskExecutionRolePolicy"
                )
            ],
        )

        batch_jofDef = batch.JobDefinition(
            self,
            "jobDef",
            platform_capabilities=[batch.PlatformCapabilities("FARGATE")],
            container=batch.JobDefinitionContainer(
                image=ecs.ContainerImage.from_asset("./tester/"),
                command=["dig", "guarddutyc2activityb.com"],
                log_configuration=batch.LogConfiguration(
                    log_driver=batch.LogDriver.AWSLOGS
                ),
                execution_role=task_execution_role,
            ),
        )
