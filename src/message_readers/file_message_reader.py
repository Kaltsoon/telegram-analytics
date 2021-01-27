import json
from message_readers.message_reader import MessageReader
from entities.message import Message


def get_message_id(message):
    message_id = message['id']

    return f'telegram:{message_id}'


def get_message_user_id(message):
    user_id = message['from_id']

    return f'telegram:{user_id}'


def get_message_text(message):
    text = message['text']

    if isinstance(text, str):
        return text

    if isinstance(text, list):
        return ' '.join([part for part in text if isinstance(part, str)])

    return ''


class FileMessageReader(MessageReader):
    def __init__(self, file_path):
        self._file_path = file_path

    def read_messages(self):
        messages = []

        with open(self._file_path) as file:
            data = json.load(file)
            json_messages = data['messages']

            messages = [Message(get_message_id(message), get_message_text(message), get_message_user_id(message))
                        for message in json_messages if message['type'] == 'message']

        return messages[:2000]
