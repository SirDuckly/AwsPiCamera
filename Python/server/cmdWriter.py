import sys

_filePath = "/home/server/cmd/cmds.txt"

def getCmdType():
    #gets the cmd type
    cmdType = sys.argv[1]
    return cmdType

def getCameraCmd():
    cCmd = sys.argv[2]
    return cCmd

def cameraCmds(cameraCmd):
    #Writes camera command
    cmdFile = open(_filePath, "a+")
    cmdFile.write("1|" + cameraCmd + "\n")
    cmdFile.close()

def getDir():
    #gets direction
    direction = sys.argv[2]
    return direction

def getAngle():
    #gets angle
    angle = sys.argv[3]
    return angle

def servoCmds(direction, angle):
    #Appened as the next script can just clear out everything
    cmdFile = open(_filePath, "a+")
    cmdFile.write("2|" + direction + "|" + angle + "\n")
    cmdFile.close()

def main():
    cmdType = getCmdType()
    if cmdType == "1":
        cCmd = getCameraCmd()
        cameraCmds(cCmd)
    elif cmdType == "2":
        direction = getDir()
        angle = getAngle()
        servoCmds(direction, angle)
    else:
        print ("Invalid command")

main()