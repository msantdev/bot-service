class User:
    def __init__(self, id, telegram_id):
        self.id = id
        self.telegram_id = telegram_id

    def to_dict(self):
        return {
            'id': self.id,
            'telegram_id': self.telegram_id,
        }
