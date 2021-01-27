from message_writers.message_writer import MessageWriter
from entities.message import Message


class DatabaseMessageWriter(MessageWriter):
    def __init__(self, connection):
        self._connection = connection

    def write_messages(self, messages):
        message_rows = [(message.id, message.text, message.user_id)
                        for message in messages]

        tags = []

        for message in messages:
            tags = tags + message.tags

        tag_rows = [(tag.category, tag.text, tag.message_id)
                    for tag in tags]

        cursor = self._connection.cursor()

        cursor.executemany(
            'insert into messages values (?, ?, ?)',
            message_rows
        )

        cursor.executemany('insert into tags values (?, ?, ?)', tag_rows)

        self._connection.commit()
