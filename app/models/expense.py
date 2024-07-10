class Expense:
    def __init__(self, id, user_id, category_id, description, amount, added_at):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.description = description
        self.amount = amount
        self.added_at = added_at

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'description': self.description,
            'amount': self.amount,
            'added_at': self.added_at.isoformat()  
        }
