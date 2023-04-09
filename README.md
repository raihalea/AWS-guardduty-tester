
# AWS GuardDuty CDK Test Project

This project is a CDK application for testing if AWS GuardDuty effectively detects security threats across several computing services.

Confirm that it is detected as Backdoor:EC2/C&CActivity.B!DNS by making a DNS query to guarddutyc2activityb.com.

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
This CDK application includes multiple stacks, and the `BaseStack` is intended for creating a VPC and is not meant for testing GuardDuty.It also sets up logging for Route53 VPC Resolver.
`BaseStack` does not need to be explicitly deployed as its dependencies are resolved.

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
Need to manually start the job to generate a DNS query.
```
cdk deploy AwsGuarddutyTesterStack/BatchEC2Stack
```
## Batch (fargate)
Need to manually start the job to generate a DNS query.
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
Need to manually start Lambda function to generate DNS queries.
```
cdk deploy AwsGuarddutyTesterStack/LambdaStack
```
## Lambda VPC
Need to manually start Lambda function to generate DNS queries.
```
cdk deploy AwsGuarddutyTesterStack/LambdaVpcStack
```

# Destroy

##  ALL
```
cdk destroy --all
```

# Result(2023/04/09)
|   | Detect | First seen | Created at |
| ----   |  ---- | ---- | ---- |
| EC2  | Yes | 21:00:34 | 21:44:24 |
| ECS(EC2) | Yes | 22:02:25 | 22:58:50 |
| ECS(Fargate) | No | - | - |
| EKS(EC2) | Yes | 00:08:54 | 00:57:43 |
| EKS(Fargate) | No | - | - |
| Batch(EC2) | Yes | 20:13:53 | 20:49:49 |
| Batch(Fargate) | No | - | - |
| App Runner | No | - | - |
| Elastic Beanstkalk | Yes | 01:34:25 | 02:44:50 |
| Lambda | No | - | - |
| Lambda(VPC) | No | - | - |
| Lightsail |  No | - | - |
