import asyncio
import bot

async def remindme(message, args):
    '''try:
        time = int(args[-1])
        message = " ".join(message[:-1])
        asyncio.sleep(time)
        await message.author.send(message)
    except:
        await message.author.send("Invalid time format, use `\help remindme` for more info...")
    
    '''
    try:
        time = int(args[-1])
    except ValueError:
        await message.channel.send("Invalid time argument. Please use a number of seconds.")

            # Combine the rest of the arguments into the reminder message
    reminder = " ".join(args[:-1])

            # Call the remind_me function with the message and time arguments
    await bot.remind_me(message,reminder, time)
    return 



