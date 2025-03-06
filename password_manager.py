import json
import os
import re
import string
from random import choices
# from secrets import compare_digest

FILE_PATH = "users_data.json"

# Validate Gmail
def validate_gmail(gmail):
    pattern = r'^[a-zA-Z0-9_]+@gmail\.com$'
    return re.match(pattern, gmail)

# Random Password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choices(characters, k=length))

# load users from file
def load_users():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return {}

# Save to File
def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)

users = load_users()
print("Welcome to the Password Manager")
print("1. Add a New User")
print("2. Search Users")
print("3. Delete a User")
print("4. Update a User")
print("5. Exit")

choice = input("Enter Your Choice (1 to 5): ")

# Adding a User
if choice == "1":
    user_id = input("Enter Your ID: ")

    if user_id in users:
        print("User ID already exists!")
    else:
        user_name = input("Enter Your Name: ").lower()
        user_age = input("Enter Your Age: ")
        user_gmail = input("Enter Your Gmail: ")

        if not validate_gmail(user_gmail):
            print("Invalid Gmail address. Please enter a valid Gmail (example@gmail.com).")
        else:
            user_password = input("Enter Your Password or Press (y) for Auto Generate: ")
            if user_password.lower() == "y":
                user_password = generate_random_password()
                print(f"Generated Password: {user_password}")

            users[user_id] = {
                "Name": user_name,
                "Age": user_age,
                "ID": user_id,
                "Gmail": user_gmail,
                "Password": user_password
            }
            save_users(users)
            print("User Saved Successfully!")

# Searching a User
elif choice == "2":
    search = input("Enter ID to Search: ")

    if search in users:
        print("User Found")
    else:
        print("User Not Found")

# Deleting a User
elif choice == "3":
    user_id = input("Enter The ID Of The User You Want To Delete: ")

    if user_id in users:  
        del users[user_id]  
        save_users(users)  
        print("User Deleted Successfully!")
    else:
        print("User not found.")

# Updating a User
elif choice == "4":
    user_id = input("Enter The ID Of The User You Want To Update: ")

    if user_id in users:
        new_name = input("Enter New Name: ").lower()
        new_age = input("Enter New Age: ")
        new_gmail = input("Enter New Gmail: ")
        if not validate_gmail(new_gmail):
            print("Invalid Gmail address. Please enter a valid Gmail (example@gmail.com).")
        else:
            new_password = input("Enter New Password or Press (y) for Auto Generate: ")
            if new_password.lower() == "y":
                new_password = generate_random_password()
                print(f"Generated Password: {new_password}")
    
            users[user_id] = {
                "Name": new_name,
                "Age": new_age,
                "ID": user_id,
                "Gmail": new_gmail,
                "Password": new_password,
            }

            save_users(users)
            print("User Updated Successfully!")
    else:
        print("User not found.")

# Exiting the Program
elif choice == "5":
    print("Exiting Password Manager. Goodbye!!!")
else:
    print("Invalid Choice! Please enter a number between 1 and 5.")
