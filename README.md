# AwsPiCamera
 AWS controlled Raspberry Pi camera

The HTML code went onto a AWS EC2 webserver, the Raspberry Pi then connects to the EC2 instance using Python sockets. The first message the Pi sends to the AWS instance is an encoded message which the server then decodes to verify the Pi is legit. The Pi then enters a conversation with the EC2 Python server. If the movement buttons are pressed on the website, the Python server will get these commands and then send them to the Raspberry Pi which will then execute the commands. All communications between the Pi and the AWS instance are encoded with a secret key which both the Pi and instance share. 
