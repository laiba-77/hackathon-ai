import json
from tools.authentication import authenticate_user
from tools.withdraw_amount import withdraw
from guardrails.input_guardrails import validate_withdrawal_amount

class ATMVirtualAgent:
    def __init__(self, user_db):
        self.user_db = user_db
        self.current_user = None
        self.chat_history = []

    def load_chat_history(self, path='chat_history.json'):
        try:
            with open(path, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            self.chat_history = []

    def save_chat_history(self, path='chat_history.json'):
        with open(path, 'w') as f:
            json.dump(self.chat_history, f, indent=2)

    def login(self, username, password):
        if authenticate_user(username, password, self.user_db):
            self.current_user = username
            self.chat_history.append({"system": f"{username} logged in."})
            return True
        else:
            self.chat_history.append({"system": "Failed login attempt."})
            return False

    def withdraw_money(self, amount):
        if self.current_user is None:
            return "You must log in first."
        if not validate_withdrawal_amount(amount):
            return "Invalid amount. Please enter a positive number."
        result = withdraw(self.current_user, amount, self.user_db)
        self.chat_history.append({"user": self.current_user, "action": f"withdraw {amount}", "result": result})
        return result

    def get_balance(self):
        if self.current_user is None:
            return "You must log in first."
        balance = self.user_db[self.current_user]['balance']
        return f"Your current balance is ${balance:.2f}"

    def logout(self):
        if self.current_user:
            self.chat_history.append({"system": f"{self.current_user} logged out."})
            self.current_user = None
            return "Logged out successfully."
        return "No user is currently logged in."
