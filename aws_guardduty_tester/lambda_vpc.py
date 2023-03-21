from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets,
)
from constructs import Construct


class LambdaVpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.Function(
            self,
            "tester",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="tester.lambda_handler",
            code=lambda_.Code.from_asset("./tester"),
            vpc=base.vpc
        )

        rule = events.Rule(
            self,
            "Rule",
            schedule=events.Schedule.rate(Duration.minutes(3)),
            targets=[targets.LambdaFunction(fn)],
        )
