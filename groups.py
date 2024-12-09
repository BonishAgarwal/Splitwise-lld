from typing import List
from expense import Expense
from users import User


class Group:
    
    def __init__(self, group_id: str, title):
        self.group_id = group_id
        self.title = title
        self.members: List[User] = []
        self.expenses: List[Expense] = []
    
    def get_group_id(self):
        return self.group_id
    
    def get_title(self):
        return self.title

    def get_all_users_in_group(self):
        for user in self.members:
            print(user.name)
    
    def add_members(self, user: User):
        self.members.append(user)
    
    def add_expenses(self, expense: Expense):
        self.expenses.append(expense)
    
    