class Message:
    def __init__(self, message_id, text, user_id, tags=None):
        self.id = message_id
        self.text = text
        self.user_id = user_id
        self.tags = tags or []

    def __str__(self):
        return self.text
