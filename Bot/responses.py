import random
import ChatGPTAPI

def get_response(message):
    prefix = '\\'
    if message[0] == prefix:
        p_message = (message.lower())[1:]
    else:
        return
    if p_message[0:4] == 'chat':
        return str(ChatGPTAPI.get_message(p_message[4:]))
    elif p_message == "roll":
        return str(random.randint(1,6))
    else:
        return "Can not understand"
