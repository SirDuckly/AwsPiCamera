import socket
import time
from cryptography.fernet import Fernet
import encry

#Function creates socket
def createSocket():
	port = 1500
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', port))
	s.listen(1)
	return s

def getCmds(clientsocket):
	try:
		cmdFile = open("cmd/cmds.txt","r")
	except:
		return
	cmdData = cmdFile.readlines()
	for line in cmdData:
		if line.find("stop") > -1:
			sendData(clientsocket, "stop")
			cmdFile.close()
			open("cmd/cmds.txt","w").close()
			return False
		#if line.find("1") != -1 or line.find("2") != -1:
		sent = sendData(clientsocket, line)
		#For comfirmation previous packet has been sent, if not next ones arent sent
		if sent == False:
			break
	cmdFile.close()
	open("cmd/cmds.txt","w").close()
	return True

def sendData(clientsocket, message):
	#Sends data to client
	if message == "":
		return
	encryMsg = encry.encryptMsg(message)
	print ("Message: " + str(encryMsg))
	clientsocket.send(bytes(str(encryMsg),"utf-8"))
	confirm = getMessage(clientsocket)
	if confirm == "received":
		print ("Comfirmed")
		return True
	else:
		return False

def getMessage(clientsocket):
	#Gets message from client
	message = clientsocket.recv(1024).decode("utf-8")
	decodedMsg = encry.decryptMsg(message)
	return decodedMsg

def MainServerLoop():
	s = createSocket()
	#Server loop
	while True:
		clientsocket, address = s.accept()
		with clientsocket:
			print(f"Connection from: {address}")
			deMsg = getMessage(clientsocket)
			if deMsg == "camera1":
				print (deMsg)
				session = True
				while session == True:
					time.sleep(1)
					print("Checking for new commands")
					session = getCmds(clientsocket)
				clientsocket.close()
			else:
				#Don't want other people connecting
				clientsocket.close()

MainServerLoop()