# Import required AWS SDK and JSON handling libraries
import boto3
import json
from botocore.exceptions import ClientError

# Initialize empty list to store conversation history
messages = []

def add_message(role, text):
    """
    Adds a message to the conversation history with specified role and text
    role: either 'user' or 'assistant'
    text: the content of the message
    """
    messages.append({"role": role, "content": [{"type": "text", "text": text}]})

def invoke_claude_model(prompt_text):
    """
    Sends a prompt to Claude 3 Sonnet model and returns the generated response
    prompt_text: the user's input text to send to the model
    """
    # Add user's prompt to conversation history
    add_message("user", prompt_text)

    # Create a Bedrock Runtime client
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    
    # Set the model ID for Claude 3 Sonnet
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
    
    # Format the request payload using the model's native structure
    # - anthropic_version: API version for Bedrock
    # - max_tokens: maximum length of response
    # - temperature: controls randomness (0.7 is moderately creative)
    # - messages: full conversation history
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
        "messages": messages
    }

    try:
        # Invoke the model with the formatted request
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body)
        )
        
        # Parse the JSON response from the model
        response_body = json.loads(response['body'].read())
        
        # Extract the generated text from the response
        generated_text = response_body['content'][0]['text']

        # Add model's response to conversation history
        add_message("assistant", generated_text)

        return generated_text

    except ClientError as error:
        # Handle any AWS API errors
        print(f"Error invoking model: {error}")
        return None

def main():
    """
    Main function that runs an interactive chat loop with the model
    """
    while True:
        # Get user input
        prompt = input("User: ")

        # Exit command
        if "exit" in prompt.lower():
            print("Exiting chat...")
            break
    
        # Get the model's response
        response = invoke_claude_model(prompt)
        
        # Print the response if successful
        if response:
            print("Model Response:")
            print(response)

# Standard Python idiom to ensure main() only runs if script is executed directly
if __name__ == "__main__":
    main()