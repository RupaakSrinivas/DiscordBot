import time
import asyncio

async def remindme(message, args):
    try:
        time = int(args[-1])
        message = " ".join(message[:-1])
        asyncio.sleep(time)
        message.author.send(message)
    except:
        message.author.send("Invalid time format, use `\help remindme` for more info...")
    



