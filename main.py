import json
import os
from password_utils import (
    analyze_password,
    generate_salt,
    hash_password,
    verify_password
)

USERS_FILE = "users.json"
MAX_ATTEMPTS = 3


# -------------------------
# File Handling
# -------------------------

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# -------------------------
# Strength Label
# -------------------------

def get_strength_label(score):
    if score < 40:
        return "Weak"
    elif score < 70:
        return "Moderate"
    else:
        return "Strong"


# -------------------------
# Registration
# -------------------------

def register(users):
    print("\n=== User Registration ===")

    username = input("Choose a username: ")

    if username in users:
        print("Username already exists.")
        return

    while True:
        password = input("Create a strong password: ")
        score, entropy, feedback = analyze_password(password)
        strength = get_strength_label(score)

        print(f"Strength: {strength}")

        if strength == "Strong":
            break
        else:
            print("Password is not strong enough.")
            for item in feedback:
                print("-", item)

    security_answer = input(
        "Security Question - What was the name of your first pet? "
    )

    salt = generate_salt()
    password_hash = hash_password(password, salt)

    users[username] = {
        "password_hash": password_hash,
        "salt": salt,
        "security_answer": security_answer.lower(),
        "failed_attempts": 0,
        "locked": False
    }

    save_users(users)
    print("Registration successful!")


# -------------------------
# Login
# -------------------------

def login(users):
    print("\n=== Login ===")

    username = input("Username: ")

    if username not in users:
        print("User not found.")
        return

    user = users[username]

    if user["locked"]:
        print("Account is locked due to too many failed attempts.")
        return

    password = input("Password: ")

    if verify_password(password, user["password_hash"], user["salt"]):
        print("Login successful!")
        user["failed_attempts"] = 0
        save_users(users)
    else:
        user["failed_attempts"] += 1
        print("Wrong password.")

        if user["failed_attempts"] >= MAX_ATTEMPTS:
            user["locked"] = True
            print("Account locked due to multiple failed attempts.")

        save_users(users)


# -------------------------
# Recover Password
# -------------------------

def recover_password(users):
    print("\n=== Password Recovery ===")

    username = input("Username: ")

    if username not in users:
        print("User not found.")
        return

    user = users[username]

    answer = input("What was the name of your first pet? ")

    if answer.lower() != user["security_answer"]:
        print("Incorrect answer.")
        return

    print("Identity verified. Create a new password.")

    while True:
        new_password = input("Enter new strong password: ")

        if verify_password(new_password, user["password_hash"], user["salt"]):
            print("You cannot reuse your old password.")
            continue

        score, entropy, feedback = analyze_password(new_password)
        strength = get_strength_label(score)

        if strength != "Strong":
            print("Password is not strong enough.")
            for item in feedback:
                print("-", item)
            continue

        new_salt = generate_salt()
        new_hash = hash_password(new_password, new_salt)

        user["password_hash"] = new_hash
        user["salt"] = new_salt
        user["failed_attempts"] = 0
        user["locked"] = False

        save_users(users)
        print("Password successfully updated.")
        break


# -------------------------
# Main Menu
# -------------------------

def main():
    users = load_users()

    while True:
        print("\n=== MAIN MENU ===")
        print("1 - Register")
        print("2 - Login")
        print("3 - Recover Password")
        print("4 - Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register(users)

        elif choice == "2":
            login(users)

        elif choice == "3":
            recover_password(users)

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()