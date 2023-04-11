import random
import ChatGPTAPI

def get_response(message):
    p_message = message.lower()

    if p_message[:5] == '\chat':
        return str(ChatGPTAPI.get_message(p_message[5:]))
    elif p_message == "roll":
        return str(random.randint(1,6))
    else:
        return "Can not understand"
