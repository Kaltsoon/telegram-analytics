class Tag:
    def __init__(self, category, text, message_id=None):
        self.category = category
        self.text = text
        self.message_id = message_id

    def __str__(self):
        return f'({self.category}, {self.text})'
