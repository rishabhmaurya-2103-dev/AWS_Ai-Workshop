import json
import boto3

# Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'  # Change to your region
)

def lambda_handler(event, context):

    # Get user message
    user_message = event.get('message', 'Hello! Who are you?')

    # Call Bedrock (Claude model)
    response = bedrock.invoke_model(
        modelId='us.anthropic.claude-sonnet-4-20250514-v1:0',
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        })
    )

    # Parse response
    response_body = json.loads(response['body'].read())
    ai_reply = response_body['content'][0]['text']

    # Return response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': ai_reply
        })
    }
