import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
chat = client.chats.create(model="gemini-3.6-flash")

print("Chatbot ready! Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    reply = chat.send_message(user_input)
    print("Bot:", reply.text)