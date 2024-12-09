from typing import List
from users import User


class Expense:
    
    def __init__(self, id, title, amount, paid_by = User):
        self.id = id
        self.title = title
        self.amount = amount
        self.paid_by_user = paid_by
        self.participants: List[User] = []
    
    def get_participants(self):
        return self.participants
    
    def get_paid_by_user(self):
        return self.paid_by_user

    def get_amount(self):
        return self.amount

    def add_participants(self, users: List[User]):
        for user in users:
            self.participants.append(user)
    
    
    
    
    
    