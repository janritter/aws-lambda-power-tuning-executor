import argparse
import boto3


def getStateMachineArnByStackName(stackName):
    client = boto3.client("cloudformation")

    response = client.describe_stacks(StackName=stackName)

    outputs = response.outputs
    for output in outputs:
        if output["OutputKey"] == "StateMachineARN":
            return output["OutputValue"]

def startStepFunctionsExecution(stateMachineARN, input):
    client = boto3.client("stepfunctions")

    response = client.start_execution(
        stateMachineArn=stateMachineARN,
        input=input
    )

    return response['executionArn']

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--stack-name",
        type=str,
        help="Name of the aws-lambda-power-tuning cloudformation stack",
        default="lambda-power-tuning",
    )

    args = parser.parse_args()

    print("Using stack-name:", args.stack_name)

    stateMachineARN = getStateMachineArnByStackName(args.stack_name)
    print("StepFunctions stateMachine ARN:", stateMachineARN)


if __name__ == "__main__":
    main()
