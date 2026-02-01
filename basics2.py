"""
Basic OpenAI Agent Example
A simple agent that uses OpenAI's API to respond to user questions and generate business ideas.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

# Load environment variables from .env file
load_dotenv(override=True)


openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI() 

messages = [{"role": "user", "content": "I want to build an app to help Juniors collaboration in order for them to be able to find a job or build a smart app by themselves that will be visible for investors or opportunities seekers"}]

# Then make the first call:

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print(response.choices[0].message.content)

# Then read the business idea:

junior_app_idea = response.choices[0].message.content

display(Markdown(junior_app_idea))

messages2 = [{"role": "user", "content": junior_app_idea}]

# Then make the first call:

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages2
)

print(response.choices[0].message.content)

# Then read the business idea:

most_valuable = response.choices[0].message.content

display(Markdown(most_valuable))