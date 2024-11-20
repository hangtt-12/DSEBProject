import json
import os

class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.user = None
        return cls._instance

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def save_user_data(self, full_name, username, password):
        JSON_FILE_PATH = 'users.json'
        # Create an empty list if the file doesn't exist
        if not os.path.exists(JSON_FILE_PATH):
            with open(JSON_FILE_PATH, 'w') as file:
                json.dump([], file)
        
        # Read existing data
        with open(JSON_FILE_PATH, 'r') as file:
            users = json.load(file)

        # Check if the username already exists
        for user in users:
            if user["username"] == username:
                return False

        user_data = {
            "full_name": full_name,
            "username": username,
            "password": password  # You should encrypt the password in a real application
        }
        users.append(user_data)

        with open(JSON_FILE_PATH, 'w') as file:
            json.dump(users, file, indent=4)
        
        print(f"User {username} has been registered successfully!")
        return True

    def load_user_data(self, username, password):
        JSON_FILE_PATH = 'users.json'
        if not os.path.exists(JSON_FILE_PATH):
            return False

        with open(JSON_FILE_PATH, 'r') as file:
            users = json.load(file)

        for user in users:
            if user["username"] == username and user["password"] == password:
                self.set_user(user)
                return True

        return False

# Initialize the singleton instance
user_manager = UserManager()