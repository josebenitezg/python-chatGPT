import os
import sys
import time
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

systemPrompt = { "role": "system", "content": "Use triple backticks with the language name for every code block in your markdown response, if any." }
data = []

def get_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
        
    
    data.append({"role": "assistant", "content": incoming_msg})
    print('THE DATA', data)
    messages = [ systemPrompt ]
    messages.extend(data)
    print('THE MESSAGES', messages)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""