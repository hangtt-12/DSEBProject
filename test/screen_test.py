import uuid
import hashlib
from kivy_sample_.encrypt.pw_encryption import MD5
md5=MD5()
# String to convert
input_string = "example_string"

# Hash the string and create a UUID
hashed = md5.encrypt(input_string)
new_uuid = uuid.UUID(hashed[:32])  # Take the first 32 characters
print(f"Generated UUID from string: {new_uuid}")