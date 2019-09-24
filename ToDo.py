ToDoList = []
RunOk = True
print()
print("add : add a new task to the list")
print("list : print all the tasks in the list")
print("mark : mark a finished task")
print("archive : delete all the marked tasks")
print("end : end program")
print()
print("Choose a command: add, list, mark, archive, end:")

try:
    with open("ToDoListFile.txt", "r") as Tlistfile:
        pass
except FileNotFoundError:
    with open("ToDoListFile.txt", "w") as Tlistfile:
        pass
else:
    with open("ToDoListFile.txt", "r") as Tlistfile:
        ToDoList = Tlistfile.readlines()
        for i in range(len(ToDoList)):
            ToDoList[i] = ToDoList[i].replace("\n","")
while RunOk:
    Szam = True
    command = input("- ")
    if (command != "add" and command != "list" and command != "mark" 
    and command != "archive" and command != "end"):
        print("Wrong command!")
    elif command == "add":
        Item = ""
        Item = input("Add a new task: ")
        ToDoList.append("[ ] " + Item)
    elif command == "list":
        sorszam = 1
        for i in ToDoList:
            print(str(sorszam) +". " + i)
            sorszam += 1
    elif command == "mark":
        sorszam = 1
        for i in ToDoList:
            print(str(sorszam) +". " + i)
            sorszam += 1
        while Szam:
            Szam = True
            print()
            M = input("Which task is completed?")
            try:
                probe = int(M)
            except TypeError:
                print("Wrong number!")
                break
            except ValueError:
                print("Wrong number!")
                break
            else:
                pass    
            if int(M) > 0 and int(M) < len(ToDoList):
                Szam = False
                ToDoList[int(M)-1] = ToDoList[int(M)-1].replace("[ ]","[X]")
                print()
    elif command == "archive":
        TempList =[]
        for i in range(len(ToDoList)):
            if ToDoList[i].find("[X]") == -1:
                TempList.append(ToDoList[i])
            else:
                pass
        ToDoList = TempList
    elif command == "end":
        with open("ToDoListFile.txt", "w") as Tlistfile:
            for item in ToDoList:
                Tlistfile.write(item + "\n")
        RunOk = False
    print()
    print("Choose a command: add, list, mark, archive, end:")
    print()
        