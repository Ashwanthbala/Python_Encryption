import os

from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "voldemort.py" or file == "decrypt.py" or file == "thekey.key":
        continue
    else:
        files.append(file)


print(files)

with open("thekey.key","rb") as fkey:
    key = fkey.read()

print(key)

for efile in files:
    with open(efile,"rb") as fdr:
        contents = fdr.read()
    decrypted_content = Fernet(key).decrypt(contents)
    with open(efile,"wb") as fdw:
        fdw.write(decrypted_content)

print("Contents have been decrypted !!!")