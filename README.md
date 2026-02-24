# 🔐 Secure Authentication System (Python)

A secure authentication system built in Python featuring salted password hashing, login attempt limits, and account lock mechanisms.

This project was developed for educational purposes to demonstrate core cybersecurity and backend authentication concepts.

---

## 🚀 Features

- Multi-user registration
- Password strength analysis
- Entropy calculation
- Common password detection
- Salted password hashing (SHA-256 + unique salt per user)
- Login attempt limit
- Automatic account lock after multiple failed attempts
- Secure password recovery with validation
- Persistent storage using JSON
- Modular architecture

---

## 🛡 Security Concepts Implemented

### 🔑 Salted Hashing

Each user has a unique random salt.  
Passwords are never stored in plain text.

Instead of:

hash(password)

I use:

hash(password + salt)

This prevents:

- Rainbow table attacks
- Identical hash detection
- Precomputed hash attacks

---

### 🚫 Account Lock Mechanism

After multiple failed login attempts:

- The account is automatically locked.
- The user must reset the password to unlock.

This simulates brute-force attack mitigation.

---

### 📊 Password Strength Analysis

Passwords are evaluated based on:

- Length
- Uppercase characters
- Lowercase characters
- Numbers
- Special characters
- Entropy calculation
- Common password detection

---

## 🧠 Technologies Used

- Python 3
- hashlib
- os
- json
- math

---

## ⚠️ Important Note

This project uses SHA-256 for educational purposes.

In production systems, password hashing should use slow hashing algorithms such as:

- bcrypt
- Argon2
- PBKDF2

These are designed to resist brute-force attacks.

---

## 📁 Project Structure

secure-auth-system/  
│  
├── main.py  
├── password_utils.py  
├── common_passwords.txt  
├── users.json (ignored)  
├── .gitignore  
└── README.md  

---

## 🔮 Future Improvements

- Implement bcrypt or Argon2
- Add timestamp-based temporary lock
- Add logging system
- Migrate from JSON to SQLite
- Convert to Flask API
- Build a web interface

---

## 🎯 Learning Objectives

This project demonstrates understanding of:

- Authentication flow
- Password security
- Hashing and salting
- Account lock logic
- Modular design
- File handling
- Defensive programming

---

## 👨‍💻 Author

Luis Moura  
Engineering Informatics Student