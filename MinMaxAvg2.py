numbers = [-5, 23, 0, "kitten", -9, 12, 99, [2, 44], None, 105, -43]
Max = numbers[0]
Min = numbers[0]
Avg = 0  
for i in numbers:
    try:
        a = int(i)
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        Avg += i
        if Max < i:
            Max = i
        if Min > i:
            Min = i
print("A legnagyobb szam: " + str(Max))
print("A legkisebb szam: " + str(Min))
print("A atlag: " + str(Avg/len(numbers)))