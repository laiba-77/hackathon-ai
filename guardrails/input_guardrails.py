def validate_withdrawal_amount(amount):
    try:
        amt = float(amount)
        return amt > 0 and amt % 10 == 0  # Only allow multiples of 10
    except (ValueError, TypeError):
        return False
