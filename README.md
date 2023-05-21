# Going serverless - introduction to AWS Lambda

This repo contains a series of introductory examples for AWS Lambda. The code examples
have an increasing level of complexity, and will progressively disclore different features
of the AWS Lambda ecosystem.

## What are you getting

The repo has the following folders:

- **/docs** - contains the slide deck that that provides the content in which the various examples are presented
- **/01-basic-example** - the "hello world" of AWS Lambda. Intended as an accessible introduction to the AWS console.
- **/02-simple-aws-http-api** - an example that uses the API Gateway to expose a Lambda function to the Internet.
- **/03-dependencies** - introduces AWS SAM, and how to add dependencies to the code.
- **/04-powertools** - introduces AWS Lambda Powertools and focuses on logs and metrics.

## Requirements

In order to run the examples you will need the following:

- Python 3 interpreter ([installation instructions](https://www.python.org/about/gettingstarted/))
- Access to an AWS account ([sign up](https://aws.amazon.com/resources/create-account/))
- AWS CLI ([installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html))
- Docker ([installation instructions](https://docs.docker.com/desktop/))
- AWS SAM CLI ([installation instructions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))

## Useful commands for SAM based examples

Example commands to do the most common tasks with the AWS SAM CLI from the root directory of each example:

- Running locally:

```bash
sam local start-api
```

- Running unit tests:

```bash
python -m pytest tests/unit -v
```

- Running integration tests: ``

```bash
# You can find the stack name for each example in `samconfig.toml`
AWS_SAM_STACK_NAME=<REPLACE WITH STACK NAME> python -m pytest tests/integration -v
```

- Deploy to AWS:

```bash
sam build && sam deploy
```
