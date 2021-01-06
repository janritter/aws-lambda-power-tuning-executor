# AWS Lambda power tuning executor

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
