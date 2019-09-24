DoorsList = []
for i in range(0,100):
    DoorsList.append("closed")
Activity = 1
for i in range(0,100):
    ActiveDoorsList = []
    for h in range(1,101):
        if h % Activity == 0:
            ActiveDoorsList.append(h-1) 
    for j in ActiveDoorsList:
        if DoorsList[j] == "closed":
            DoorsList[j] = "open"
        else:
            DoorsList[j] = "closed"
    Activity += 1
print()
print("After 100 runs...")
print()
z = 0
for k in range(100):
    if DoorsList[k] == "open":
        print("The " + str(k+1) + ". door is " + (DoorsList[k]) + ".")
        z += 1
print()
print("Totally " + str(z) + " doors is open.")
print()