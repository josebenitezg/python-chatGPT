import os
import sys
import time
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(question):
    print(question)
    data = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return data.choices[0].message['content']