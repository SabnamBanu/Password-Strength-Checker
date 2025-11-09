import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    if len(password) < 6:
        remarks = "Password too short. Minimum 6 characters required."
        return "Weak", remarks
    else:
        if len(password) >= 8:
            strength += 1
        if re.search("[a-z]", password):
            strength += 1
        if re.search("[A-Z]", password):
            strength += 1
        if re.search("[0-9]", password):
            strength += 1
        if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            strength += 1

    if strength <= 2:
        return "Weak", "Your password could be easily guessed."
    elif strength == 3 or strength == 4:
        return "Medium", "Your password is okay, but could be stronger."
    else:
        return "Strong", "Your password is strong."

# Main Program
if __name__ == "__main__":
    pwd = input("Enter Password: ")
    strength, remarks = check_password_strength(pwd)
    print(f"Password Strength: {strength}")
    print(f"Remarks: {remarks}")



