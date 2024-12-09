from typing import Dict, List
from expense import Expense
from groups import Group
from users import User


class SplitwiseService:
    
    _instance = None
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, Group] = {}
        
        if SplitwiseService._instance is not None:
            SplitwiseService._instance = self
        
        return SplitwiseService._instance

    def add_users(self, user: User):
        self.users[str(user.get_user_id())] = user
    
    def add_groups(self, group: Group):
        self.groups[str(group.get_group_id())] = group


    def add_expense(self, group_id: str, expense: Expense, participants: List[User]):

        group = self.groups[str(group_id)]
        expense.add_participants(participants)
        
        if group:
            group.add_expenses(expense)
            self.update_balance(expense)
    
    def update_balance(self, expense: Expense):
        paid_by_user = expense.get_paid_by_user()
        participants = expense.get_participants()
        amount = expense.get_amount()
        
        paid_by_user.add_balance(amount, participants)
    
     