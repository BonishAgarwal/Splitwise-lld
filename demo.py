from users import User
from groups import Group
from expense import Expense

from splitwise_service import SplitwiseService



def main():
    
    split_service = SplitwiseService()
    
    # Create users
    user1 = User("1", "Alice", "alice@example.com", "1234567890")
    user2 = User("2", "Bob", "bob@example.com", "1234567890")
    user3 = User("3", "Charlie", "charlie@example.com", "1234567890")

    split_service.add_users(user1)
    split_service.add_users(user2)
    split_service.add_users(user3)
    
    # Create a group
    group = Group("1", "Apartment")
    group.add_members(user1)
    group.add_members(user2)
    group.add_members(user3)
    
    split_service.add_groups(group)
    
    expense = Expense("1", "Rent", 300.0, user1)
    
    
    split_service.add_expense(group.get_group_id(), expense, participants=[user1, user2])

    
    print(user1.get_balances())

if __name__ == "__main__":
    main()