import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

_filePath = "/home/pi/Documents/client/security/key.txt"

#checks key file exists 
def checkKey():
    if os.path.exists(_filePath):
        return
    else:
        createKey()

def createKey():
    #Uses this random string for the password to base the
    #encryption off
    keyPwd = 'xvx_vWI!c$"f.T[aGXR)=-?prv]tl2'
    pwd = keyPwd.encode() #Coverts pwd to bytes/ encodes it
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

def deleteKey():
    #If key file exists, it deletes it
    if os.path.exists(_filePath):
        os.remove(_filePath)
    else:
        print("File doesn't exist")

def encryptMsg(msg):
    #Checks for keyfile
    checkKey()
    keyFile = open(_filePath, "rb")
    key = keyFile.read()
    keyFile.close()
    encoded = msg.encode()
    #Uses the key to encrypt the message with fernet
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    #Returns encrypted message
    return encrypted

def decryptMsg(encryptedMsg):
    #Decode
    checkKey()
    #gets key from keyfile
    keyFile = open(_filePath, "rb")
    key = keyFile.read()
    keyFile.close()
    #Uses a key with fernet to decrypt the message
    f2 = Fernet(key)
    #If its turned back to bytes it'll add b' at the start and ' at the end
    #this will break the decryption process so these extra characters are removed
    encryptedMsg = encryptedMsg[2:-1]
    byteMsg = bytes(encryptedMsg, "utf-8")
    decrypt = f2.decrypt(byteMsg)
    originalMsg = decrypt.decode()
    return originalMsg