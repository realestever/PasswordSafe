import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''

'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
'''

masterPwd = input("Enter master password: ")

# if salt file does not exist then create one
if not os.path.exists("salt.bin"):
    with open('salt.bin', 'wb') as f:
        f.write(os.urandom(16))

with open('salt.bin', 'rb') as f:
    salt=f.read()

kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=1_200_000)
key = base64.urlsafe_b64encode(kdf.derive(masterPwd.encode()))
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # print(passw)
            # print(passw.encode())
            print("User: ", user, "\nPassword: ", fer.decrypt(passw.encode()).decode(), "\n")


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    # using with will remove the need to close the file
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


if __name__ == '__main__':
    while True:
        mode = input("View existing passwords or add new password (view, add) \nPress \"q\" to quit\n").lower()
        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
            continue

