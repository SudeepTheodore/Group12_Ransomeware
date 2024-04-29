import os
from cryptography.fernet import Fernet

def algorithem_data(file_path, key):
    with open(file_path, "rb") as thefile:
        contents_encrypted = thefile.read()
    try:
        contents_decrypted = Fernet(key).decrypt(contents_encrypted)
        with open(file_path, "wb") as thefile:
            thefile.write(contents_decrypted)
        print(f"Decrypted {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")

def algorithem_decrypt(directory_path, key):
    for foldername, subfolders, filenames in os.walk(directory_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            if filename not in ["encrpt.py", "decrypt.py", "edkey.key"]:
                algorithem_data(file_path, key)


key_file_path = os.path.join(os.getcwd(), "edkey.key")
with open(key_file_path, "rb") as edkey:
    key = edkey.read()

# Decrypt files in the current directory
for file in os.listdir():
    if os.path.isfile(file):
        file_path = os.path.join(os.getcwd(), file)
        algorithem_data(file_path, key)

# Decrypt files in child folders
current_directory = os.getcwd()
algorithem_decrypt(current_directory, key)
