# AWS Lambda Power Tuning Executor

> Script to easily execute the [AWS Lamba Power Tuning state machine](https://github.com/alexcasalboni/aws-lambda-power-tuning) with different config files

## Prerequisites

- Python3
- Pip

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

```bash
python3 executor.py --stack-name serverlessrepo-lambda-power-tuner --config my-test.json
```

A documentation for the input configuration can be found [here](https://github.com/alexcasalboni/aws-lambda-power-tuning/blob/master/README-INPUT-OUTPUT.md#user-content-state-machine-input)
