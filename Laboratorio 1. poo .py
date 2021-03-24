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
    win = 0
    if player1 > a:
        win = 1
    if player2 > a:
        win = 2
    if player1 == player2 == a:
        win = 3
    if player1 != player2 != a:
        win = 0
    return win

#Remueve la carta de la lista total, cuando un jugador logra una correcta
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
#Funcion encargada de organizar las cartas y asignarles coord
def cardlist(cartas,total):
    i = 0
    i2 = 0
    a = int(total/2)
    part1 = []
    part2 = []
    part1b = []
    part2b = []

    while i < a:
        part1.append(cartas[i])
        part1b.append("1,"+ str(i+1))
        i+=1
    while a < total:
        part2.append(cartas[a])
        part2b.append("2,"+ str(i2+1))
        i2+=1
        a+=1
    return part1,part2,part1b,part2b


#######################################################################

a = int(input("Ingrese número de cartas a jugar por jugador\n"))

playerturn1 = 1
playerturn2 = 0
player1score = 0
player2score = 0

cartas = cardmaker(a)
total = len(cartas)

#Bucle de juego principal
win = 0
choice = 0
choice2 = 0

while win == 0:
    if playerturn1 == 1:
        print("turno jugador 1")
        choice = input()
        choice2 = input()
        if choice != choice2:
            playerturn1 = 0
            playerturn2 = 1
            choice = 0
            choice2 = 0
        else:
            player1score+=1
            win = wincondition(total,player1score,player2score)
            playerturn1 = 1
            playerturn2 = 0
            print(player1score)
            print(win)

    if playerturn2 == 1:
        print("turno jugador 2")
        choice = input()
        choice2 = input()
        if choice != choice2:
            playerturn1 = 1
            playerturn2 = 0
            choice = 0
            choice2 = 0
        else:
            player2score+=1
            win = wincondition(total,player1score,player2score)
            playerturn1 = 0
            playerturn2 = 1
            print(player2score)
            print(win)

    else:
        pass
        
        
        
    
    






