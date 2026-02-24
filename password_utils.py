import math
import hashlib
import os


# -------------------------
# Entropy Calculation
# -------------------------

def calculate_entropy(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(not c.isalnum() for c in password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)


# -------------------------
# Common Password Check
# -------------------------

def check_common_password(password):
    try:
        with open("common_passwords.txt", "r") as file:
            common = file.read().splitlines()
            return password in common
    except FileNotFoundError:
        return False


# -------------------------
# Password Analysis
# -------------------------

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 25
    else:
        feedback.append("Use at least 12 characters.")

    if any(c.islower() for c in password):
        score += 15
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 15
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 15
    else:
        feedback.append("Add numbers.")

    if any(not c.isalnum() for c in password):
        score += 15
    else:
        feedback.append("Add special characters.")

    if check_common_password(password):
        score -= 30
        feedback.append("This is a very common password.")

    entropy = calculate_entropy(password)

    return score, entropy, feedback


# -------------------------
# Secure Hashing with Salt
# -------------------------

def generate_salt():
    return os.urandom(16).hex()


def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()


def verify_password(password, stored_hash, salt):
    return hash_password(password, salt) == stored_hash