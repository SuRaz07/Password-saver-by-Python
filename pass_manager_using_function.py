import json
import os
import re
import string
from random import choices

FILE_PATH = "users_data_func.json"

# Validate Gmail
def validate_gmail(gmail):
    pattern = r'^[a-zA-Z0-9_]+@gmail\.com$'
    return re.match(pattern, gmail)

# Generate Random Password
def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(choices(characters, k=length))

# Load Users from JSON File
def load_users():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return {}

# Save Users to JSON File
def save_users(users):
    with open(FILE_PATH, "w") as file:
        json.dump(users, file, indent=4)
        
try:
    users = load_users()
except:
    users= {}

#Add a User

def add_user():
    user_id = input("Enter Your ID: ")
    user_name = input("Enter Your Name: ").lower()
    user_age = input("Enter Your Age: ")
    user_gmail = input("Enter Your Gmail: ")
    if not validate_gmail(user_gmail):
        print("Invalid Gmail address. Please enter a valid Gmail (example@gmail.com).")
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

    # Search by ID
def search_user():
    users = load_users()
    search_id = input("Enter ID to Search: ")
    if search_id in users:
        print("User Found")
    else:
        print("User Not Found")

#  Delete a User
def delete_user():
    users = load_users()
    delete_id = input("Enter The ID Of The User You Want To Delete: ")
    if delete_id in users:
        del users[delete_id]
        save_users(users)
        print("User Deleted Successfully!")
    else:
        print("User Not Found.")

# Update a User
def update_user():
    users = load_users()
    update_id = input("Enter The ID Of The User You Want To Update: ")

    if update_id in users:
        new_name = input("Enter New Name: ").lower()
        new_age = input("Enter New Age: ")
        new_gmail = input("Enter New Gmail: ")
        new_password = input("Enter New Password or Press (y) for Auto Generate: ")

        if new_password.lower() == "y":
            new_password = generate_random_password()
            print(f"Generated Password: {new_password}")

        # Update user info
        users[update_id] = {
            "Name": new_name,
            "Age": new_age,
            "ID": user_id,
            "Gmail": new_gmail,
            "Password": new_password
        }

        save_users(users)
        print("User Updated Successfully!")
    else:
        print("User Not Found.")
 
    
print("Welcome to the Password Manager")
print("1. Add a New User")
print("2. Search Users")
print("3. Delete a User")
print("4. Update a User")
print("5. Exit")

choice = input("Enter Your Choice (1 to 5): ")

if choice == "1":
        add_user()
elif choice =="2":
        search_user()
elif choice == "3":
        delete_user()
elif choice == "4":
        update_user()
elif choice == "5":
        print("Exiting Password Manager")
else: 
    print("Invalued Choice, Please enter a numbers b/w 1 to 5")