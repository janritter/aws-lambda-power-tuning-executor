import argparse
import boto3
import time
import progressbar
import json


def getStateMachineArnByStackName(stackName):
    client = boto3.client("cloudformation")

    response = client.describe_stacks(StackName=stackName)

    outputs = response['Stacks'][0]['Outputs']
    for output in outputs:
        if output["OutputKey"] == "StateMachineARN":
            return output["OutputValue"]

def startStepFunctionsExecution(stateMachineARN, input):
    client = boto3.client("stepfunctions")

    response = client.start_execution(
        stateMachineArn=stateMachineARN,
        input=input
    )

    executionARN = response['executionArn']
    print("Execution started with ARN:",executionARN)

    return executionARN

def checkExecutionStatus(executionARN):
    client = boto3.client("stepfunctions")

    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    runningChecks = 0

    while True:
        response = client.describe_execution(
            executionArn=executionARN
        )

        status = response['status']
        
        if (status == "RUNNING"):
            runningChecks = runningChecks + 1
            bar.update(runningChecks)
            time.sleep(0.5)

        elif (status == "FAILED"):
            bar.finish()
            print("The execution failed, check the Step Functions console for more information")
            break

        else:
            bar.finish()
            print("\n----------\nStatus:", status)
            print("Execution output:")
            print(json.dumps(json.loads(response['output']), indent=4))
            break

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--stack-name",
        type=str,
        help="Name of the aws-lambda-power-tuning cloudformation stack",
        default="lambda-power-tuning",
    )

    parser.add_argument(
        "--config",
        type=str,
        help="File name of the config used for testing",
        default="",
    )

    args = parser.parse_args()

    print("Using stack-name:", args.stack_name)

    stateMachineARN = getStateMachineArnByStackName(args.stack_name)
    print("Step Functions state machine ARN:", stateMachineARN)

    print("\n----------\nLoading config from: "+args.config)
    configContent = open(args.config, 'r').read()

    executionARN = startStepFunctionsExecution(stateMachineARN, configContent)
    checkExecutionStatus(executionARN)

if __name__ == "__main__":
    main()
