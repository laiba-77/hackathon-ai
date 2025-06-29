def withdraw(username, amount, user_db):
    amount = float(amount)
    user = user_db.get(username)
    if not user:
        return "User not found."
    if amount > user['balance']:
        return "Insufficient funds."
    user['balance'] -= amount
    return f"Withdrawal of ${amount:.2f} successful. New balance: ${user['balance']:.2f}"
