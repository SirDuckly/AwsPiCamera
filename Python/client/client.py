import socket
import os
import encry
import execCmd

def connect():
	#Function for connecting to server
	svr = "35.176.182.169"
	port = 1500
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((svr, port))
	except socket.error as e:
		error = f"Error while connecting: {e}"
		return error
	return s

def disconnect(socket):
	#Closes connection
	socket.close()

def checkConnection(socket):
	#Checks connection has been made and is able to send data
	try:
		socket.send("check")
		return socket
	except socket.error as e:
		#returns connection failed
		error = f"Error while connecting: {e}"
		return error
	#if try except is missed somehow just default to con failed
	return "Error"

def getMessage(socket):
	#Function to get messages from server
	srvMsg = socket.recv(1024).decode("utf-8")
	if str(srvMsg) == "":
		return "noMsg"
	decodedMsg = encry.decryptMsg(srvMsg)
	return decodedMsg

def sendReceivedMsg(socket):
	#Sends a received message to the server which lets it know
	#the client is ready for the next message
	comfirm = encry.encryptMsg("received")
	socket.send(bytes(str(comfirm), "utf-8"))

def clientLoop(socket):
	#Used to authenticate with server
	usrNm = "camera1"
	#Send encrypted
	eMsg = encry.encryptMsg(usrNm)
	socket.send(bytes(str(eMsg), "utf-8"))
	while True:
		#Blue LED is on for the duration of the session
		os.system('sudo ./piiotest writepin 21 1')
		#Decrypts the message from the server
		decodedMsg = getMessage(socket)
		#Executes the command sent from the server
		execCmd.getCmdType(decodedMsg)
		#Stops it trying to send received message when nothing has been sent
		if decodedMsg != "noMsg":
			sendReceivedMsg(socket)
			if decodedMsg == "stop":
				os.system('sudo ./piiotest blink 16 5')
				#WORKS
				break
	os.system('sudo ./piiotest writepin 21 0')
	disconnect(socket)

def main():
	#Tries to connect
	s = connect()
	#If returns "Error" the socket connection hasn't been made
	try:
		s.find("Error")
		print (s)
	except:
		#If connection has been made go into clientLoop
		clientLoop(s)
		return

main()