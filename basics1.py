"""
Basic OpenAI starting point
A simple agent that uses OpenAI's API to respond to user queries.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv(override=True)


openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

openai = OpenAI() 
messages = [{"role": "user", "content": "What is 2+2?"}]
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.7,
    max_tokens=500
)
print(response.choices[0].message.content)

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": question}]

# ask it - this uses GPT 4.1 mini, still cheap but more powerful than nano
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

question = response.choices[0].message.content

print(question)

messages = [{"role": "user", "content": question}]

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

answer = response.choices[0].message.content
print(answer)

# Initialize OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# def run_agent(user_message: str) -> str:
#     """
#     Run the agent with a user message and return the response.
    
#     Args:
#         user_message: The message from the user
        
#     Returns:
#         The agent's response as a string
#     """
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": user_message}
#             ],
#             temperature=0.7,
#             max_tokens=500
#         )
        
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error: {str(e)}"


# def main():
#     """Main function to run the agent interactively."""
#     print("🤖 Basic OpenAI Agent")
#     print("Type 'exit' to quit\n")
    
#     while True:
#         user_input = input("You: ")
        
#         if user_input.lower() in ['exit', 'quit']:
#             print("Goodbye!")
#             break
        
#         if user_input.strip():
#             print("Agent: ", end="", flush=True)
#             response = run_agent(user_input)
#             print(response)
#             print()


# if __name__ == "__main__":
#     main()
