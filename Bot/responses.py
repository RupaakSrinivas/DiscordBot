import random
import ChatGPTAPI
import reminder
#import help

def get_response(message):
    prefix = '\\'
    user_message = str(message.content)
    if user_message[0] == prefix:
        command, *args = message.content[len(prefix):].split()
        print(command, args)
    else:
        return
    if command == "roll":
        return str(random.randint(1,6))
    elif command == "hello":
        return "Hello !"
    elif command == "chatgpt":
        return ChatGPTAPI.get_message(" ".join(args))
    #elif command == "help":
     #   return help.help(args)
    elif command == "remindme":
        reminder.remindme(message, args)
        return 
    elif command == "remindall":
        return reminder.remind(args)
    else:
        return "Invalid command, use \help to learn more..."
