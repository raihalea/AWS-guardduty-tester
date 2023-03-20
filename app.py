#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_guardduty_tester.aws_guardduty_tester_stack import AwsGuarddutyTesterStack

app = cdk.App()

AwsGuarddutyTesterStack(app, "AwsGuarddutyTesterStack",)

app.synth()
