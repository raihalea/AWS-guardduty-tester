from aws_cdk import (
    Stack,
    aws_s3_assets as assets,
    aws_elasticbeanstalk as elasticbeanstalk,
    aws_iam as iam,
)
from constructs import Construct


class ElasticBeanstalkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        asset = assets.Asset(self, "tester", path="./tester/")

        application = elasticbeanstalk.CfnApplication(
            self, "Application", application_name="guardduty-test"
        )

        app_version = elasticbeanstalk.CfnApplicationVersion(
            self,
            "appVersion",
            application_name=application.application_name,
            source_bundle=elasticbeanstalk.CfnApplicationVersion.SourceBundleProperty(
                s3_bucket=asset.s3_bucket_name, s3_key=asset.s3_object_key
            ),
        )
        app_version.add_dependency(application)

        instance_role = iam.Role(
            self, "instanceRole", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        instance_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AWSElasticBeanstalkWebTier")
        )
        instance_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AWSElasticBeanstalkMulticontainerDocker"
            )
        )

        instance_profile = iam.CfnInstanceProfile(
            self, "instanceProfile", roles=[instance_role.role_name]
        )

        environment = elasticbeanstalk.CfnEnvironment(
            self,
            "Environment",
            application_name=application.application_name,
            solution_stack_name="64bit Amazon Linux 2 v3.5.5 running Docker",
            option_settings=[
                elasticbeanstalk.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:autoscaling:launchconfiguration",
                    option_name="IamInstanceProfile",
                    value=instance_profile.ref,
                )
            ],
            version_label=app_version.ref,
        )
        environment.add_dependency(application)
