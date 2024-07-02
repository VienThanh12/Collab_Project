import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key = os.environ.get("OPENAI_API_KEY")
)


def generate_description(input):
    messages = [
        {"role": "user",
            "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = completion.choices[0].message
    return reply


def message_to_chat_gpt(input):
    messages = [
        {"role": "user",
            "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = completion.choices[0].message
    return reply