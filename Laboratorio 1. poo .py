import random

def cardmaker(num):
    i = 1
    list = []
    num2 = num + 1
    while i < num2:
        list.append(i)
        list.append(i)
        i+=1
        random.shuffle(list)
    return list

a = int(input("Ingrese número de cartas a jugar por jugador"))


print(a*2," cartas totales")

print(cardmaker(a))
