numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
Max = -50000
Min = 50000
Avg = 0  
for i in numbers:
    Avg += i
    if Max < i:
        Max = i
    if Min > i:
        Min = i
print("A legnagyobb szam: " + str(Max))
print("A legkisebb szam: " + str(Min))
print("A atlag: " + str(Avg/len(numbers)))