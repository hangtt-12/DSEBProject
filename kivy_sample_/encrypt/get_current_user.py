import json
from user_manager import User
def get_current_user(json_file_path):
    users = []
    try:
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("JSON data should be a list of dictionaries.")
        users = [User.from_dict(entry) for entry in data if entry.get("status") is True]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return users