# AWS Lambda Power Tuning Executor

> Script to easily execute the [AWS Lamba Power Tuning state machine](https://github.com/alexcasalboni/aws-lambda-power-tuning) with different config files

## Prerequisites

- Python3
- Pip
- Lambda Power Tuning tool installed in AWS (see [how to deploy](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/33fda7d77abadc660cb1a7869d5d47e5869fdda1/README-DEPLOY.md))

## Setup

### Create venv

```bash
python3 -m venv env
```

### Activate venv

```bash
source ./env/bin/activate
```

### Install requirements

```bash
pip3 install -r requirements.txt
```

## Usage

1. Login to the account containing the Lambda Power Tuning tool
2. Execute the Lambda Power Tuning tool (replace the stack-name flag with your stack name)
    1.  ```bash
        python3 executor.py --stack-name serverlessrepo-lambda-power-tuner --config my-test.json
        ```

A documentation for the input configuration can be found [here](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README-INPUT-OUTPUT.md#user-content-state-machine-input)
