angle = input()
currAngle = -20
print ("Given angle: " + str(angle) + "\nCurrAngle: " + str(currAngle))
newAngle = int(currAngle) + -abs(int(angle))
if newAngle <= -90:
    diff = abs(-90-newAngle)
    newAngle = newAngle +diff
print ("Final angle: " + str(newAngle))