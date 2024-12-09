from typing import Dict


class User:
    
    def __init__(self, user_id: str, name: str, email: str, contact: str):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.contact = contact
        self.balances: Dict[str, float] = {} # This will keep track of balances of particular user with its friends
    
    def get_user_id(self):
        return self.user_id
    
    def get_email(self):
        return self.email

    def get_name(self):
        return self.name
    
    def get_contact(self):
        return self.contact

    def get_balances(self):
        return self.balances

    def add_balance(self, amount: int, participants):
        
        number_of_participants = len(participants) + 1
        
        splitted_amount = amount // number_of_participants
        
        for participant in participants:
            self.balances[participant.get_user_id()] = splitted_amount