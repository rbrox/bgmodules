from openai import OpenAI

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key

client = OpenAI(api_key=api_key)
def generate_response(prompt, data):
    """
    Generates a response from the OpenAI GPT model given a prompt and some data.

    Parameters:
    - prompt: A string representing the instruction or question.
    - data: A string representing additional context or data to assist in generating the response.

    Returns:
    - The generated response text.
    """
    # Create a chat completion request with the given prompt and data
    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful teaching assitant in Philosophy based on the books written by AC Bhaktivedanta Srila Prabhupad."},
        {"role": "user", "content": f"{prompt} {data}"}
    ])

    # Extract and return the generated text from the assistant's reply
    return response.choices[0].message.content

# Example usage
prompt = "What is"
data = "the soul"
response_text = generate_response(prompt, data)
print(response_text)
