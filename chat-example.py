import os
import dotenv
import openai
import json

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

print("run openai API...")
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
]
print("messages:")
print(json.dumps(messages, indent=4))
print("=" * 40)

resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

print("response:")
print("=" * 40)
print(resp)
print("=" * 40)
