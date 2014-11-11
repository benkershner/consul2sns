consul2sns
==========

Publish state changes from Consul to AWS SNS.

## Usage

On one of the Consul servers, run the following command:
`consul watch -type=check cat | ./consul2sns.py -t foo-bar`

## Pre-reqs

The following Python modules are required:

 - boto

## Command Line Options

-  `-t, --topic TOPIC` The AWS SNS topic ARN to publish to. This is an expanding 
  ARN, meaning it will make assumptions to fill in the whole ARN; using the
  region selected and the AWS account ID of the Boto user. This means that you
  can use *just* the SNS topic name (e.g. `foobar`) and it will expand it to the
  full ARN (e.g. `arn:aws:sns:us-east-1:123456789012:foobar`).
-  `-r, --region REGION` The AWS region to connect to.
-  `-f, --filter FILTER` The state transition filter, which is a JSON dictionary
  of state changes that will be passed to SNS. Default is all state changes. The
  valid states are:
  - `passing`
  - `warning`
  - `critical`
  For example, if the dictionary was `{"warning": ["critical", "passing"], 
  "critical": ["passing"]}`, it would only forward state transitions from
  warning to critical or passing, and from critical to passing.
- `--escalation` Only forward escalating states (from `passing` up to
  `critical`).
- `--de-escalation` Only forward de-escalating states (from `critical` down to
  `passing`).
- `--access-key-id ACCESS_KEY_ID` The AWS IAM access key ID. You should use
  `boto.cfg` instead.
- `--secret-access-key SECRET_ACCESS_KEY` The AWS IAM secret access key. You
  should use `boto.cfg` instead.
- `-v, --verbose` Print verbose output.
