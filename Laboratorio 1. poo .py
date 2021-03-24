import random

#Crea una lista con los numeros asociados a cada carta
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

#Identifica si ambos valores de carta son iguales o no
def checker(num1,num2):
    if num1 == num2:
        a = True
    if num1 != num2:
        a = False
    return a

#Checkea la condicion del juego:
#1 si el jugador 1 gana
#2 si el jugador 2 gana
#3 si se produce un empate
#0 si el juego continua
def wincondition(total,player1,player2):
    a = (total/2)
    if player1 > a:
        win = 1
    if player2 > a:
        win = 2
    if player1 == player2 == a:
        win = 3
    if player1 != player2 != a:
        win = 0
    return win

def cardremove(card,lista):
    a = []
    i = 0
    while i < len(lista):
        if lista[i] != card:
            a.append(lista[i])
            i+=1
        else:
            i+=1
    return a
    
    
a = int(input("Ingrese número de cartas a jugar por jugador\n"))

player1 = 0
player2 = 0
player1score = 0
player2score = 0

cartas = cardmaker(a)
total = len(cartas)

print(cartas)

print(cardremove(1,cartas))
