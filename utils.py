import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
chat_id_list = json.loads(config.get('DEFAULT', 'chat_ids'))


def can_reply_to_chat_id(message):
    chat_id = message.chat.id
    if chat_id in chat_id_list:
        return True
    else:
        return False


def extract_message(arg):
    return arg.split()[1]
