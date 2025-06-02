#------------------------------------------------------------------------------------
# Created by Rama Subramanyam based on video at youtube at https://www.youtube.com/watch?v=vmNeZ9-S6dQ
# This is the first one in the series to learn implementation serverless app at AWS
# 
# date : May 2025
# usage: over ride default variable values
#------------------------------------------------------------------------------------

###################################################
# Lambda Runtime Settings  
# lambda_python_runtime = "python3.9"
# debug_mode = true
# lambda_siz = 256
# lambda_timeout = 400

####################################################
# Lambda Environment Variable Settings
# API_KEY = "<openai-key>"
####################################################


import openai
import os


def lambda_handler(event, context):
    # Get Environment variable  
    openai.api_key = os.getenv("API_KEY")

    # API key validation
    if not openai.api_key:
        html_output = "<html><body><h1>Error</h1><p>API key not set.</p></body></html>"
        return {
            'statusCode': 500,
            'body': html_output,
            'headers': {
                'Content-Type': 'text/html'
            }
        }

    # Set value for location for which you would like to display interesting fact to user
    location = "New York, NY"
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Tell me interesting fact about {location} in less than 200 characters "}
    ]

    try:
        # chat = openai.Completion.create(model="gpt-3.5-turbo", messages = messages)
        chat = openai.chat.completions.create(model="gpt-3.5-turbo", messages = messages)
        gpt_response = chat.choices[0].message.content
        html_output = f"<html><body><h1>Interesting Fact about the place {location}</h1><p>{gpt_response}</p></body></html>"
        print("gpt_response:", gpt_response)
        status_code = 200
    except Exception as e:
        html_output = f"<html><body><h1>Error</h1><p>Failed to get response from OpenAI API: {str(e)}</p></body></html>"
        print("OpenAI API error:", str(e))
        status_code = 500

    return {
        'statusCode': status_code,
        'body': html_output,
        'headers': {
            'Content-Type': 'text/html'
        }
    }
