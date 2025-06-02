# Lambda-OpenAI-Interface-Example1

[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)
[![GitHub](https://a11ybadges.com/badge?logo=github)](https://a11ybadges.com/badge?logo=github)
[![GitHubActions](https://a11ybadges.com/badge?logo=githubactions)](https://a11ybadges.com/badge?logo=githubactions)
<BR>

# **Description**

A simple [AWS Serverless](https://aws.amazon.com/serverless/) - [Lambda](https://aws.amazon.com/lambda/) application with a simple interface to Open AI to get interesting facts of a predefined location. It is implementation of [example applications](https://platform.openai.com/examples) found in the official OpenAI API documentation.

This is a first practice example to start learning to implement serverless application with the OpenAI interfaces.

# **Architecture**

Below is the architecture diagram with flow of data across the different components of AWS

[Architecture diagram](./docs/Lambda-OpenAI-Interface-Example1.jpg)![Architecture diagram](./docs/Lambda-OpenAI-Interface-Example1.jpg)

# **Quick Start**

Works with Linux, Windows, and macOS environments

Verify Project requirements: [AWS Account](https://aws.amazon.com/free/) and [Python 3.11](https://www.python.org/). For those who wants to use AWS CLI, then [CLI](https://aws.amazon.com/cli/) access

### Implementation Steps

```
1. Create lambda function with code from
   lambda_Landing_Page.py
   - Runtime - Python3.9 or above
   - Timeout - 40 sec

2. Add environment variables API_KEY
    - Go to Configuraiton tab & Environment Vairables Menu
    - key : API_KEY
    - value :Paste the key you get from https://platform.openai.com/ website

3. Create function URL.
    - Go to Configuraiton tab & Function URL Menu
    - Create (Auth Type - None) Function URL

4. Create Zip file of python openai libraries. This can be done either locally in your system or through Cloud 9.
    - Go To Cloud 9 Environment - Crate environment - Then open - Go to AWS Tab (left hand side)
    - Go to lambda function under the region (on the left hand side). Go the the directory where the lambda function code is available
    -   Download the code.  In the terminal install openai libraries using command like "pip3 install openai --target  ."
    - UPload the openai libraries using the zip command

5. Deploy Lambda function
    - Back to  Lambda function.  Refresh the page
    - Deploy the funciton & test
6.  Access the lambda function from the browser using the Function URL copied in step Step 3

7. deployLambdaFunction.yml helps to deploy function using GitHub Actions. If planned to use GitHub Actions, then make the following changes to  [deployLambdaFunction.yml](./.github/workflows/deployLambdaFunction.yml)
    - Change the lambda function ARN in lines 29 & 38
    - Change AWS_DEFAULT_REGION in lines 34 & 46 with correct region
    - Add secret keys AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY with values in GitHub Repository

```
