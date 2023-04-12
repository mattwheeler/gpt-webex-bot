import os
import openai
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
WEBEX_ACCESS_TOKEN = os.getenv("WEBEX_ACCESS_TOKEN")
WEBEX_API_URL = "https://webexapis.com/v1/messages"

headers = {
    "Authorization": f"Bearer {WEBEX_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


def process_prompt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()


@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    user_id = data["data"]["personId"]
    room_id = data["data"]["roomId"]
    message_id = data["data"]["id"]

    message_response = requests.get(
        f"{WEBEX_API_URL}/{message_id}",
        headers=headers
    )

    message_text = message_response.json()["text"].strip()

    if message_text.startswith("@webexwiz"):
        prompt = message_text[len("@webexwiz"):].strip()
        gpt_response = process_prompt(prompt)

        message_data = {
            "roomId": room_id,
            "text": gpt_response
        }

        requests.post(
            WEBEX_API_URL,
            json=message_data,
            headers=headers
        )

    return "OK"


if __name__ == "__main__":
    app.run()
