#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from "@aws-cdk/core";
import { FargateDemoStack } from '../lib/fargate';

const app = new cdk.App();
new FargateDemoStack(app, 'FargateDemoStack', {
    env: { account: '059252037207', region: 'us-east-1' },
  /* For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html */
});