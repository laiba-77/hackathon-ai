import hashlib

def authenticate_user(username, password, user_db):
    user = user_db.get(username)
    if not user:
        return False
    # Simple password hash check (for demo only)
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed == user['password_hash']
