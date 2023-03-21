import os
import openai
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request

# A comment to change the  git hash and commit.
app = Flask(__name__)
slack_app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

# Set up GPT-3 API client
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Function to generate GPT-3 response
def generate_gpt3_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant, deployed to a Hackerspace Slack channel. You will assist with diy projects, hacking, making, infosec, CTFs and ALL other queries from members."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            n=1,
            temperature=0.5,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating GPT-4 response: {e}")
        print(f"Error details: {e.args}")
        return None

# Fetch user's display name or real name
def fetch_username(user_id):
    try:
        result = client.users_info(user=user_id)
        user = result["user"]
        return user.get("profile", {}).get("display_name") or user.get("real_name")
    except Exception as e:
        print(f"Error fetching user's display name: {e}")
        return "unknown user"

def fetch_conversation_history(channel, thread_ts, bot_user_id):
    try:
        result = client.conversations_replies(
            channel=channel,
            ts=thread_ts,
        )
        messages = result["messages"]
        conversation_history = ""
        for message in messages:
            timestamp = message["ts"]
            user_id = message["user"]
            text = message["text"]
            username = fetch_username(user_id) if user_id != bot_user_id else "gpt-4"
            conversation_history += f"[{timestamp}] {username}: {text} "
        return conversation_history
    except Exception as e:
        print(f"Error fetching conversation history: {e}")
        return ""

@slack_app.event("message")
def handle_message_events(body, logger):
    event = body['event']
    text = event.get('text', '')
    if event.get("channel_type") not in ("channel", "im"):
        return

    # Get the bot_user_id
    bot_user_id = client.auth_test()['user_id']

    if event["channel_type"] == "im" or (event["channel_type"] == "channel" and f"<@{bot_user_id}>" in text):
        # Fetch the user's display name or real name
        slack_username = fetch_username(event["user"])
        
        # Fetch conversation history from the thread
        conversation_history = fetch_conversation_history(event["channel"], event["thread_ts"], bot_user_id) if "thread_ts" in event else ""

        stripped_text = text.replace(f"<@{bot_user_id}>", "").strip()
        prompt = f"Conversation History: {conversation_history} New Query:: {slack_username}: {stripped_text}"
        
        response = generate_gpt3_response(prompt)

        if response:
            client.chat_postMessage(channel=event['channel'], thread_ts=event.get('ts'), text=response)
        else:
            client.chat_postMessage(channel=event['channel'], thread_ts=event.get('ts'), text="Sorry, I couldn't generate a response. Please try again.")

handler = SlackRequestHandler(slack_app)

@app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
