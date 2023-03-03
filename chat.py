import os
import sys
import time
import openai

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    message = input('\n')
    data = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    delay_print(data.choices[0].message['content'])
