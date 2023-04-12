import discord
import responses
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

token = os.getenv('TOKEN')

async def send_message(message, is_private):
    try:
        response = responses.get_response(message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)
async def remind_me(message,reminder, time):
    await asyncio.sleep(time)
    await message.channel.send(reminder)

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client( intents = intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, is_private = True)
        else:
            await send_message(message, is_private = False)
    client.run(token)
 