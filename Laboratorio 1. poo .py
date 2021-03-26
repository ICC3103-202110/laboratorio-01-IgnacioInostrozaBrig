import random
#ver Lab1 ver0.7
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

#Checkea la condicion del juego:
#1 si el jugador 1 gana #2 si el jugador 2 gana
#3 si se produce un empate #0 si el juego continua
def wincondition(total,player1,player2):
    a = float((total/2))
    print(a)
    win = 0
    if (float(player1)) > (a):
        win = 1
    if float(player2) > a:
        win = 2
    if float(player1) == float(player2) == a:
        win = 3
    return win

#Funcion encargada de organizar las cartas y asignarles coord
def cardlist(cartas,total):
    i = 0
    i2 = 0
    b = int(total)
    a = int(total/2)
    part1 = []
    part2 = []
    while i < a:
        part1.append([cartas[i],("1,"+ str(i+1))])
        i+=1
    while a < b:
        part2.append([cartas[a],("2,"+ str(i2+1))])
        i2+=1
        a+=1
    return part1,part2

def initialcards(cartas,total):
    i = 0
    i2 = 0
    b = int(total)
    a = int(total/2)
    part1 = []
    part2 = []
    while i < a:
        part1.append([" ? ",("1,"+ str(i+1))])
        i+=1
    while a < b:
        part2.append([" ? ",("2,"+ str(i2+1))])
        i2+=1
        a+=1
    return part1,part2
#######################################################################

a = int(input("Ingrese número de cartas a jugar por jugador\n"))

playerturn1 = 1
playerturn2 = 0
player1score = 0
player2score = 0
print("\n")
cartas = cardmaker(a/2)
total = a/2
part1 = cardlist(cartas,len(cartas))[0]
part2 = cardlist(cartas,len(cartas))[1]
part3 = initialcards(cartas,len(cartas))[0]
part4 = initialcards(cartas,len(cartas))[1]
print("TABLERO INICIAL\n")
print(part3)
print(part4)
print("\n")
#Bucle de juego principal
win = 0
choice = 0
choice2 = 0

while win == 0:
    if playerturn1 == 1:
        print("turno jugador 1")
        choice = str(input())
        choice2 = str(input())
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
        choice = str(input())
        choice2 = str(input())
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
    if win == 1:
        print("Gana jugador 1")
        break
    if win == 2:
        print("Gana jugador 2")
        break
    if win == 3:
        print("Empate")
        break
        
        
        
    
    







