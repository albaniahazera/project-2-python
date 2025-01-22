from cryptography.fernet import Fernet
import getpass
import os, time

#start login function 
def generate_key():
    key = Fernet.generate_key()
    if not os.path.exists("secure_data"):
        os.makedirs("secure_data")
    with open("secure_data/secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secure_data/secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def save_credentials(username, password):
    encrypted_username = encrypt_message(username)
    encrypted_password = encrypt_message(password)
    with open("secure_data/credentials.txt", "wb") as cred_file:
        cred_file.write(encrypted_username + b"\n" + encrypted_password)

def load_credentials():
    if not os.path.exists("secure_data/credentials.txt"):
        return None, None
    with open("secure_data/credentials.txt", "rb") as cred_file:
        lines = cred_file.readlines()
        encrypted_username = lines[0].strip()
        encrypted_password = lines[1].strip()
        username = decrypt_message(encrypted_username)
        password = decrypt_message(encrypted_password)
        return username, password

def login():
    if not os.path.exists("secure_data/secret.key"):
        generate_key()
    
    username, password = load_credentials()
    if username and password:
        print(f"Welcome back, {username}!")
    else:
        print("\n\t\tFirst time setup\n")
        username = input("Enter your username: ")
        while True:
            password = getpass.getpass("Enter new password: ")
            confirm_password = getpass.getpass("Confirm new password: ")
            if password == confirm_password:
                break
            else:
                os.system("clear")
                print("Passwords do not match. Please try again.")
        save_credentials(username, password)
        print("Data has saved !")
# end login function

if __name__ == "__main__":
    login()