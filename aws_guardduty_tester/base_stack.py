from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_logs as logs,
    aws_route53resolver as route53resolver,
)
from constructs import Construct
import boto3


class BaseStack(Stack):
    @property
    def vpc(self):
        return self._vpc

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._vpc = ec2.Vpc(self, "vpc", nat_gateways=1)

        log_group_name = "/guardduty-tester/" + self.stack_name

        boto3_logs = boto3.client("logs")
        res = boto3_logs.describe_log_groups(logGroupNamePattern=log_group_name)
        if res["logGroups"]:
            self._log_group = logs.LogGroup.from_log_group_name(
                self, "Log Group", log_group_name=log_group_name
            )
        else:
            self._log_group = logs.LogGroup(
                self,
                "Log Group",
                log_group_name=log_group_name,
                retention=logs.RetentionDays.ONE_DAY,
            )

        self.resolver_logging = route53resolver.CfnResolverQueryLoggingConfig(
            self, "DNSlogging", destination_arn=self._log_group.log_group_arn
        )

        self._resolver_logging_associate = (
            route53resolver.CfnResolverQueryLoggingConfigAssociation(
                self,
                "DNSloggingAssociate",
                resolver_query_log_config_id=self.resolver_logging.attr_id,
                resource_id=self._vpc.vpc_id,
            )
        )
