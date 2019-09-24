import os

#####
def stringReplaceI(string,where,what): # Stringben cserel x.-ik elemet valamire
    tempS = ""
    for i in range(len(string)):
        if i != int(where):
            tempS += string[i]
        else:
            tempS += what
    return tempS
#####
# koordinata ellenorzes hajoblokkok elhelyezesehez
def CoordLimitCheck(ship):
    ship_segment = []
    for i in ship:
        if i != ",":

    for x in ship_segment:
        b = 0
        if len(x) == 1 and x == "E":
            return False
        if len(x) != 2:
            #print("hosszerr")
            return True  
        try:
            b = int(x[1])
        except TypeError:
            #print("typerr")
            return True
        except ValueError:
            #print("valerr")
            return True   
        else:
            pass
        if (int(x[1]) >= 0 and int(x[1]) <= 9 and ord(x[0]) >= 65 and ord(x[0]) <= 74):
            return False
        else:
            #print("enderr")
            return True
#####################
def Admiralis():
    TempFleet = []
    for i in range(2): # 5 hajos limit    
        print("Add meg a hajoblokk koordinatajat (ha befejezted adj meg egy E betut): ")
        print()
        TempShip = []
        NotBigEnough = True
        while NotBigEnough: # 4 blokkos limit
            if len(TempShip) == 4: # 4 blokkos limit
                print("Eleg nagy mar ez a hajo!")
                NotBigEnough = False
            InputNotOk = True
            while InputNotOk: 
                TempCoord = (input("Uj hajo koordinatai: "))
                InputNotOk = CoordLimitCheck(TempCoord)
                if InputNotOk == True:
                    print("Hibas, add meg ujra: ")
            if TempCoord == "E":
                break    
            TempShip = TempCoord
        TempFleet.append(TempShip)
    print("Az " + str(i+1) + ". hajo a terkepen!")
    return TempFleet
####################
def generateRows(): # vizualis valtozokat keszit a flottanak
    for x in AFleet: # x egy hajo
        for y in x: # y egy koordinata
            if y[0] == "A":
                z = y[1]
                Map[0] = stringReplaceI(Map[0],z,chr(9619))
            if y[0] == "B":
                z = y[1]
                Map[1] = stringReplaceI(Map[1],z,chr(9619))
            if y[0] == "C":
                z = y[1]
                Map[2] = stringReplaceI(Map[2],z,chr(9619))
            if y[0] == "D":
                z = y[1]
                Map[3] = stringReplaceI(Map[3],z,chr(9619))
            if y[0] == "E":
                z = y[1]
                Map[4] = stringReplaceI(Map[4],z,chr(9619))
            if y[0] == "F":
                z = y[1]
                Map[5] = stringReplaceI(Map[5],z,chr(9619))
            if y[0] == "G":
                z = y[1]
                Map[6] = stringReplaceI(Map[6],z,chr(9619))
            if y[0] == "H":
                z = y[1]
                Map[7] = stringReplaceI(Map[7],z,chr(9619))
            if y[0] == "I":
                z = y[1]
                Map[8] = stringReplaceI(Map[8],z,chr(9619))
            if y[0] == "J":
                z = y[1]
                Map[9] = stringReplaceI(Map[9],z,chr(9619))
#######
def Visual(): #rajzol
    os.system("clear")
    Head1 = "    0 1 2 3 4 5 6 7 8 9"
    Head2 = "   ---------------------"
    Foot = Head2
    Oszlop ="ABCDEFGHIJ"
    print()
    print("Battleship (ver. alpha 0.0001)")
    print()
    print(Head1)
    print(Head2)
    for i in range(10): 
        print(Oszlop[i] + " |", end = "")
        for d in Map[i]:
            print(d*2, end = "")
        print(" |")
    print(Foot)
######
def Visual_Init(): #rajzol
    os.system("clear")
    print()
    print("Battleship (ver. alpha 0.0001)")
    print()
    print(Head1)
    print(Head2)
    for i in range(10): 
        print(Oszlop[i] + " |                    |")
    print(Foot)
# Global variables def part
Map = []
for tenger in range(10):
    Map.append("          ")
AFleet =[]
BFleet =[]
Head1 = "    0 1 2 3 4 5 6 7 8 9"
Head2 = "   ---------------------"
Foot = Head2
Oszlop ="ABCDEFGHIJ"
# Global var def end
Visual_Init()
print()
print("A hajóblokkok elhelyezesehez meg kell adni a koordinákat, mint pl. A2, F8.")
print()
AFleet = Admiralis()
Visual()
#print("A B jatekos jon")
#BFleet = Admiralis() kikapcsolva ideiglenesen
generateRows() 
Visual()               


#print(chr(9617))               
               
#print(chr(9619))               