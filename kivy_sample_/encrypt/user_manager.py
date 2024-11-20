import os
import json
from kivy_sample_.encrypt.pw_encryption import MD5
md5 = MD5()

def encrypt_passw(password):
    return md5.calculate(password)

class User:
    def __init__(self, full_name, username, password, status=False):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.status = status
        self.notes = []
        self.todo_list_done = []
        self.todo_list_undone = []
        self.achievements = []

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "username": self.username,
            "password": self.password,
            "status": self.status,
            "notes": self.notes,
            "todo_list_done": self.todo_list_done,
            "todo_list_undone": self.todo_list_undone,
            "achievements": self.achievements
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["full_name"], 
            data["username"], 
            data["password"],
            data.get("status", False)
        )
        user.notes = data.get("notes", [])
        user.todo_list_done = data.get("todo_list_done", [])
        user.todo_list_undone = data.get("todo_list_undone", [])
        user.achievements = data.get("achievements", [])
        return user


    @classmethod
    def get_current_user(cls, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON data should be a list of dictionaries.")

            for entry in data:
                if entry.get("status") is True:
                    return cls.from_dict(entry)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading JSON file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return None
    @classmethod
    def reset_all_status(cls, json_file_path):
        try:
            # Read the data from the JSON file
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            if not isinstance(data, list):
                raise ValueError("JSON data should be a list of dictionaries.")

            # Update the status of all users to False
            for entry in data:
                entry["status"] = False

            # Save the updated data back to the file
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print("All user statuses have been set to False.")

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading or writing JSON file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    def add_note(self, note):
        self.notes.append(note)

    def remove_note(self, note):
        if note in self.notes:
            self.notes.remove(note)
        else:
            print("Note not found.")

    def add_todo(self, todo_item):
        self.todo_list.append({"task": todo_item, "completed": False})

    def remove_todo(self, todo_item):
        for item in self.todo_list:
            if item["task"] == todo_item:
                self.todo_list.remove(item)
                return
        print("Todo item not found.")

    def complete_todo(self, todo_item):
        for item in self.todo_list:
            if item["task"] == todo_item:
                item["completed"] = True
                return
        print("Todo item not found.")

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def remove_achievement(self, achievement):
        if achievement in self.achievements:
            self.achievements.remove(achievement)
        else:
            print("Achievement not found.")

    def save_user_data(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            for i, entry in enumerate(data):
                if entry["username"] == self.username:
                    data[i] = self.to_dict()
                    break
            else:
                data.append(self.to_dict())

            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)

            print("User data saved successfully.")

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error reading or writing JSON file: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

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

    def register_user(self, full_name, username, password,status=False):
        if self.check_username_exists(username):
            return False
        encrypted_password = encrypt_passw(password)
        new_user = User(full_name, username, encrypted_password,status=status)
        
        users = self.load_users()
        users.append(new_user)
        self.save_users(users)
        return True

    def login_user(self, username, password):
        users = self.load_users()
        for user in users:
            if user.username == username and user.password == encrypt_passw(password):
                user.status = True
                self.current_user = user
                print(f"Current user: {self.current_user.full_name if self.current_user else None}")
                self.save_users(users)
                return True
        return False

    def get_current_user(self):
        return self.current_user




