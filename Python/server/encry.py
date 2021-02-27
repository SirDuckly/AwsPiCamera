import base64
import os
#Encryption modules
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Server filepath
_filePath = "/home/server/security/key.txt"

#checks key exists 
def checkKey():
    if os.path.exists(_filePath):
        return
    else:
        createKey()

def createKey():
    keyPwd = 'xvx_vWI!c$"f.T[aGXR)=-?prv]tl2'
    pwd = keyPwd.encode() #Coverts pwd to bytes
    #salt creation
    salt = b'\xa3\x10\\>\x96\xfe(\xadA\x8b\x03>+\xf1\x11a'
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    #creates the key
    key = base64.urlsafe_b64encode(kdf.derive(pwd))
    #Saves key to file
    keyFile = open(_filePath, "wb")
    keyFile.write(key)
    keyFile.close()

#deletes current keyfile
def deleteKey():
    if os.path.exists(_filePath):
        os.remove(_filePath)
    else:
        print("File doesn't exist")

def encryptMsg(msg):
    #Encrypts the message for sending
    checkKey()
    keyFile = open(_filePath, "rb")
    key = keyFile.read()
    keyFile.close()
    encoded = msg.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted

def decryptMsg(encryptedMsg):
    checkKey()
    keyFile = open(_filePath, "rb")
    key = keyFile.read()
    keyFile.close()
    f2 = Fernet(key)
    #If the message is turned back to bytes it'll add the characters b' at the start 
    # and ' at the end
    #this WILL break the decryption process so these extra characters are removed
    encryptedMsg = encryptedMsg[2:-1]
    byteMsg = bytes(encryptedMsg, "utf-8")
    decrypt = f2.decrypt(byteMsg)
    originalMsg = decrypt.decode()
    return originalMsg