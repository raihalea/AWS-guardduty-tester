
# AWS GuardDuty CDK Test Project

This project is a CDK application for testing if AWS GuardDuty effectively detects security threats across several computing services.

## Getting Started
### Setup

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

# Running the Tests

## List
```
cdk ls
AwsGuarddutyTesterStack
AwsGuarddutyTesterStack/AppRunnerStack
AwsGuarddutyTesterStack/BaseStack
AwsGuarddutyTesterStack/ElasticBeanstalkStack
AwsGuarddutyTesterStack/LambdaStack
AwsGuarddutyTesterStack/LightsailStack
AwsGuarddutyTesterStack/BatchEC2Stack
AwsGuarddutyTesterStack/BatchFargateStack
AwsGuarddutyTesterStack/Cloud9Stack
AwsGuarddutyTesterStack/EKsEc2Stack
AwsGuarddutyTesterStack/EKsFargateStack
AwsGuarddutyTesterStack/Ec2Stack
AwsGuarddutyTesterStack/EcsEc2Stack
AwsGuarddutyTesterStack/EcsFargateStack
AwsGuarddutyTesterStack/LambdaVpcStack
```

## Base
```
cdk deploy AwsGuarddutyTesterStack/BaseStack
```

## EC2
```
cdk deploy AwsGuarddutyTesterStack/Ec2Stack
```
## ECS (EC2)
```
cdk deploy AwsGuarddutyTesterStack/EcsEc2Stackcdk
```
## ECS (Fargate)
```
cdk deploy AwsGuarddutyTesterStack/EcsFargateStack
```
## EKS(EC2)
```
cdk deploy AwsGuarddutyTesterStack/EKsEc2Stack
```
## EKS(Fargate)
```
cdk deploy AwsGuarddutyTesterStack/EKsFargateStack
```
## Batch (EC2)
```
cdk deploy AwsGuarddutyTesterStack/BatchEC2Stack
```
## Batch (fargate)
```
cdk deploy AwsGuarddutyTesterStack/BatchFargateStack
```
## App Runner
```
cdk deploy AwsGuarddutyTesterStack/AppRunnerStack
```
## Elastic Beanstkalk
```
cdk deploy AwsGuarddutyTesterStack/ElasticBeanstalkStack
```
## Lambda
```
cdk deploy AwsGuarddutyTesterStack/LambdaStack
```
## Lambda VPC
```
cdk deploy AwsGuarddutyTesterStack/LambdaVpcStack
```

# Destroy

##  ALL
```
cdk destroy --all
```