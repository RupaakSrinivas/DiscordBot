import openai
import os
from dotenv import load_dotenv
messages = None
def get_message(message):
    global messages
    load_dotenv()
    api_key = os.getenv('API_KEY')
    openai.api_key = api_key 
    if message == "quit":
        messages = None
    if messages == None:
        messages = [ {"role": "system", "content": "You are a intelligent assistent"} ]
    if message:
        messages.append(
            {"role":"user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = messages
        )
        reply = chat .choices[0].message.content
        messages.append( {"role": "assistant", "content": reply} )
    return str(reply)