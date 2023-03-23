import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def chatGPT(question):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question},
    ]
    print("messages:")
    print(json.dumps(messages, indent=4))
    print("=" * 40)

    resp = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    print("response:")
    print("=" * 40)
    print(resp)
    print("=" * 40)
    
    return resp



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = chatGPT(question)
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)
