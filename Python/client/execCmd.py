import os
import pantilthat
from picamera import PiCamera
from time import sleep

def getCmdType(message):
    split = message.split("|")
    if split[0] == "1":
        #Split 1 can only be takePic currently
        cameraCmd(split[1])
    elif split[0] == "2":
        #Split 1 = direction, split 2 = angle
        workOutDirection(split[1], int(split[2]))
    else:
        return

def cameraCmd(camCmd):
    #This was going to display the image on the website but wasn't able to 
    #develop this feature in time
    if camCmd == "takePic":
        camera = PiCamera()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')


def workOutDirection(direction, angle):
    #The servos work on a scale of -90 to 90
    #So this works out if the direction is going towards the
    #negative or positive side
    if direction == "left":
        directionPositive("pan", angle)
    elif direction == "right":
        directionNegative("pan", angle)
    elif direction == "up":
        directionNegative("tilt", angle)
    elif direction == "down":
        directionPositive("tilt", angle)

def directionNegative(direction, angle):
    #Function for setting the new angle
    #and for turing on the LED's
    if direction == "tilt":
        currAngle = pantilthat.get_tilt()
        newAngle = servoFormulaNegative(currAngle, angle)
        os.system('sudo ./piiotest blink 20 1')
        pantilthat.tilt(newAngle)
        os.system('sudo ./piiotest blink 20 0')
    elif direction == "pan":
        currAngle = pantilthat.get_pan()
        newAngle = servoFormulaNegative(currAngle, angle)
        os.system('sudo ./piiotest writepin 20 1')
        pantilthat.pan(newAngle)
        os.system('sudo ./piiotest writepin 20 0')
    
def servoFormulaNegative(currAngle, angle):
    #Formula for working out new servo angle
    if currAngle <= 0:
        newAngle = currAngle + -abs(angle)
        if newAngle <= -90:
            diff = abs(-90-newAngle)
            newAngle += diff
            return newAngle
    else:
        newAngle = currAngle - angle
        return newAngle
    return newAngle

def directionPositive(direction, angle):
    #Function for setting the new angle
    #and for turing on the LED's
    if direction == "tilt":
        currAngle = pantilthat.get_tilt()
        newAngle = servoFormulaPositive(currAngle, angle)
        os.system('sudo ./piiotest blink 20 1')
        pantilthat.tilt(newAngle)
        os.system('sudo ./piiotest blink 20 0')
    elif direction == "pan":
        currAngle = pantilthat.get_pan()
        newAngle = servoFormulaPositive(currAngle, angle)
        os.system('sudo ./piiotest writepin 20 1')
        pantilthat.pan(newAngle)
        os.system('sudo ./piiotest writepin 20 0')

def servoFormulaPositive(currAngle, angle):
    #Formula for working out new servo angle
    newAngle = currAngle + angle
    if newAngle > 90:
        diff = abs(90-newAngle)
        newAngle = newAngle - diff
        return newAngle
    else:
        return newAngle
    
