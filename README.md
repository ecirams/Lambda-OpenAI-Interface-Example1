# Lambda-OpenAI-Interface-Example1

[![OpenAI](https://a11ybadges.com/badge?logo=openai)](https://platform.openai.com/)
[![Amazon AWS](https://a11ybadges.com/badge?logo=amazonaws)](https://aws.amazon.com/)
[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)
<BR>

**Description**

A simple [AWS Serverless](https://aws.amazon.com/serverless/) - [Lambda](https://aws.amazon.com/lambda/) application with a simple interface to Open AI to get interesting facts of a predefined location. It is implementation of [example applications](https://platform.openai.com/examples) found in the official OpenAI API documentation.

This is a first practice example to start learning to implement the OpenAI interfaces.

# Quick Start

Works with Linux, Windows, and macOS environments

Step 1 Verify Project requirements: [AWS Account](https://aws.amazon.com/free/), [OpenAI Platform key](https://platform.openai.com/settings/organization/api-keys) <BR>
Step 2 Login to AWS - Go to Lambda Console - Create Function with the following values<BR>
            Name - "myChatGptLambda (example)<BR>
            Runtime - Python3.9  and all others are default values<BR>
Step 3 Code Source - Copy the code available at the GIT repository lambda_function.py<BR>
Step 4 Go to Configuration Tab - General Configuration - Edit - Change Timeout as 40 sec<BR>
Step 5 Configuration Tab - Environment Variables - Edit - Add Environment variable and save<BR>
                Key - API_KEY<BR>
                Value - Paste the key you get from https://platform.openai.com/ website <BR>
Step 6 Configuration Tab - Function URL - Create (Auth Type - None) Copy Function URL to access<BR> 
Step 7 Go To Cloud 9 Environment - Crate environment - Then open - Go to AWS Tab (left hand side) <BR>
Step 8 Go to lambda function under the region. Go the the directory where the lambda function code is available<BR>
Step 9 Download the code.  In the terminal install openai libraries using command like "pip3 install openai --target  ."<BR>
Step 10 UPload the openai libraries using the zip command<BR>
Step 11 Back to Lambda screen - deploy.  <BR>
Step 12 - Access the lambda function from the browser using the Function URL copied in step Step 5.<BR>
