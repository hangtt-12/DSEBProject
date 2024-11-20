import os
import json
from kivy_sample_.encrypt.pw_encryption import MD5
md5 = MD5()

def encrypt_passw(password):
    return md5.calculate(password)

class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["full_name"], data["username"], data["password"])

class UserManager:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.current_user = None

    def load_users(self):
        if not os.path.exists(self.json_file_path):
            return []
        with open(self.json_file_path, 'r') as file:
            users_data = json.load(file)
        return [User.from_dict(user_data) for user_data in users_data]

    def save_users(self, users):
        users_data = [user.to_dict() for user in users]
        with open(self.json_file_path, 'w') as file:
            json.dump(users_data, file, indent=4)

    def check_username_exists(self, username):
        users = self.load_users()
        for user in users:
            if user.username == username:
                return True
        return False

    def register_user(self, full_name, username, password):
        if self.check_username_exists(username):
            return False
        encrypted_password = encrypt_passw(password)
        new_user = User(full_name, username, encrypted_password)
        users = self.load_users()
        users.append(new_user)
        self.save_users(users)
        return True

    def login_user(self, username, password):
        users = self.load_users()
        for user in users:
            if user.username == username and user.password == encrypt_passw(password):
                self.current_user = user
                print(f"Current user: {self.current_user.full_name if self.current_user else None}")
                return True
        return False

    def get_current_user(self):
        return self.current_user