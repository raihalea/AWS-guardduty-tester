from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_ecr_assets as assets,
    aws_iam as iam,
)
from constructs import Construct


class EksFargateStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, base, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cluster = eks.FargateCluster(
            self,
            "Cluster",
            vpc=base.vpc,
            version=eks.KubernetesVersion.V1_24,
        )

        cluster.admin_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW, resources=["*"], actions=["eks:*"]
            )
        )

        ecr_asset = assets.DockerImageAsset(self, "tester", directory="./tester")
        image_url = ecr_asset.image_uri

        cluster.add_manifest(
            "mypod",
            {
                "apiVersion": "v1",
                "kind": "Pod",
                "metadata": {"name": "mypod"},
                "spec": {"containers": [{"name": "tester", "image": image_url}]},
            },
        )