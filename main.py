import sys
import hashlib
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from my_agent.atm_agent import ATMVirtualAgent


def load_user_db():
    # For demo: One user with username 'alice', password 'password123'
    return {
        "alice": {
            "password_hash": hashlib.sha256("password123".encode()).hexdigest(),
            "balance": 1000.0
        }
    }

def main():
    user_db = load_user_db()
    agent = ATMVirtualAgent(user_db)
    agent.load_chat_history()

    print("Welcome to the AI Virtual ATM!")
    while True:
        print("\nOptions: [login] [withdraw] [balance] [logout] [exit]")
        choice = input("Choose an option: ").strip().lower()
        if choice == "login":
            username = input("Username: ")
            password = input("Password: ")
            if agent.login(username, password):
                print("Login successful.")
            else:
                print("Login failed.")
        elif choice == "withdraw":
            amount = input("Enter amount to withdraw: ")
            print(agent.withdraw_money(amount))
        elif choice == "balance":
            print(agent.get_balance())
        elif choice == "logout":
            print(agent.logout())
        elif choice == "exit":
            agent.save_chat_history()
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == '__main__':
    main()
