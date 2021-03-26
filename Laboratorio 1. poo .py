import random
#ver Lab1 ver1.0
#Creates a random list with every possible card number
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

#Checks game condition: 1.Player1 wins 2.Player2 wins
# 3. If there's a tie and 0. if the game continues as normal
def wincondition(total,player1,player2):
    a = float((total/2))
    win = 0
    if (float(player1)) > (a):
        win = 1
    if float(player2) > a:
        win = 2
    if float(player1) == float(player2) == a:
        win = 3
    return win

#Organizes cards and cordinates
def cardlist(cards,total):
    i = 0
    i2 = 0
    b = int(total)
    a = int(total/2)
    part1 = []
    part2 = []
    partx = []
    while i < a:
        part1.append([cards[i],("1,"+ str(i+1))])
        partx.append([cards[i],("1,"+ str(i+1))])
        i+=1
    while a < b:
        part2.append([cards[a],("2,"+ str(i2+1))])
        partx.append([cards[a],("2,"+ str(i2+1))])
        i2+=1
        a+=1
    
    return part1,part2,partx

#Builds initial board
def initialcards(cards,total):
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

#Finds specific card value using the cordinates
def cardfinder(cards,coord):
    for card in cards:
        if card[1] == coord:
            value = card[0]
            return value
    return False

#######################################################################
print("\n")
a = int(input("Enter number of total cards to play (Must be pair)\n"))
playerturn1 = 1
playerturn2 = 0
player1score = 0
player2score = 0
print("\n")
cards = cardmaker(a/2)
total = a/2
partx = cardlist(cards,len(cards))[2]
part1 = cardlist(cards,len(cards))[0]
part2 = cardlist(cards,len(cards))[1]
part3 = initialcards(cards,len(cards))[0]
part4 = initialcards(cards,len(cards))[1]

#Main game loop
win = 0
choice = 0
choice2 = 0
value1 = 0
value2 = 0
i3 = 0
i4 = 0
print("INITIAL BOARD\n")
print("\n")
while win == 0:
    print(part3)
    print(part4)
    print("\n")
    if playerturn1 == 1:
        print("Player 1 turn\n")
        choice = str(input())
        value1 = cardfinder(partx, choice)
        while i3 < len(part3):
            if choice == part3[i3][1]:
                part3[i3][0] = " "+str(value1)+" "
                i3+=1
            else:
                i3+=1
        while i4 < len(part4):
            if choice == part4[i4][1]:
                part4[i4][0] =" "+str(value1)+" "
                i4+=1
            else:
                i4+=1

        print("Player selected card: ", choice)
        print("\n")
        print(part3)
        print(part4)
        choice2 = str(input())
        value2 = cardfinder(partx, choice2)
        i3 = 0
        i4 = 0
        while i3 < len(part3):
            if choice2 == part3[i3][1]:
                part3[i3][0] = " "+str(value2)+" "
                i3+=1
            else:
                i3+=1
        while i4 < len(part4):
            if choice2 == part4[i4][1]:
                part4[i4][0] =" "+str(value2)+" "
                i4+=1
            else:
                i4+=1
        print("Player selected card: ", choice2)
        print("\n")
        print(part3)
        print(part4)
        i3 = 0
        i4 = 0
        k = 0
        k2 = 0
        if value1 != value2:
            print("Incorrect!\n")
            playerturn1 = 0
            playerturn2 = 1
            while k < len(part3):
                if choice == part3[k][1]:
                    part3[k][0] = " ? "
                    k+=1
                if choice2 == part3[k][1]:
                    part3[k][0] = " ? "
                    k+=1
                else:
                    k+=1
            while k2 < len(part4):
                if choice == part4[k2][1]:
                    part4[k2][0] = " ? "
                    k2+=1
                if choice2 == part4[k2][1]:
                    part4[k2][0] = " ? "
                    k2+=1
                else:
                    k2+=1
            k = 0
            k2 = 0
            choice = 0
            choice2 = 0
            value1 = 0
            value2 = 0
        else:
            print("Correct! turn will repeat\n")
            player1score+=1
            win = wincondition(total,player1score,player2score)
            playerturn1 = 1
            playerturn2 = 0
            value1 = 0
            value2 = 0

    if playerturn2 == 1:
        print("Player 2 turn\n")
        choice = str(input())
        value1 = cardfinder(partx, choice)
        while i3 < len(part3):
            if choice == part3[i3][1]:
                part3[i3][0] = " "+str(value1)+" "
                i3+=1
            else:
                i3+=1
        while i4 < len(part4):
            if choice == part4[i4][1]:
                part4[i4][0] =" "+str(value1)+" "
                i4+=1
            else:
                i4+=1

        print("Player selected card: ", choice)
        print("\n")
        print(part3)
        print(part4)
        choice2 = str(input())
        value2 = cardfinder(partx, choice2)
        i3 = 0
        i4 = 0
        while i3 < len(part3):
            if choice2 == part3[i3][1]:
                part3[i3][0] = " "+str(value2)+" "
                i3+=1
            else:
                i3+=1
        while i4 < len(part4):
            if choice2 == part4[i4][1]:
                part4[i4][0] =" "+str(value2)+" "
                i4+=1
            else:
                i4+=1
        print("Player selected card: ", choice2)
        print("\n")
        print(part3)
        print(part4)
        i3 = 0
        i4 = 0
        k = 0
        k2 = 0
        if value1 != value2:
            print("Incorrect!\n")
            playerturn1 = 1
            playerturn2 = 0
            while k < len(part3):
                if choice == part3[k][1]:
                    part3[k][0] = " ? "
                    k+=1
                if choice2 == part3[k][1]:
                    part3[k][0] = " ? "
                    k+=1
                else:
                    k+=1
            while k2 < len(part4):
                if choice == part4[k2][1]:
                    part4[k2][0] = " ? "
                    k2+=1
                if choice2 == part4[k2][1]:
                    part4[k2][0] = " ? "
                    k2+=1
                else:
                    k2+=1
            k = 0
            k2 = 0
            choice = 0
            choice2 = 0
            value1 = 0
            value2 = 0
        else:
            print("Correct! turn will repeat\n")
            player2score+=1
            win = wincondition(total,player1score,player2score)
            playerturn1 = 0
            playerturn2 = 1
            value1 = 0
            value2 = 0

    if win == 1:
        print("Player 1 wins\n")
        break
    if win == 2:
        print("Player 2 wins\n")
        break
    if win == 3:
        print(" Tie \n")
        break
        
        
        
    
    







