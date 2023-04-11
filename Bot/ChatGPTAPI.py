import openai
import os
from dotenv import load_dotenv

'''load_dotenv()

api_key = os.getenv('API_KEY')

openai.api_key = api_key
#messages = [ {"role": "system", "content": "You are a intelligent assistent."} ]
'''
'''message = ""
while message != "quit":
    message = input("User : ")
    if message:
        messages.append(
            {"role":"user","content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append( {"role": "assistant", "content": reply} )
print(messages)'''
def get_message(message):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    openai.api_key = api_key
    messages = [ {"role": "system", "content": "You are a intelligent assistent."} ]
    if message:
        messages.append(
            {"role":"user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages
        )
        reply = chat .choices[0].message.content
        #print(f"CHatGPT: {reply}")
    return str(reply)