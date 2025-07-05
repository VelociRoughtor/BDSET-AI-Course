import random

m1 = "Paper"
m2 = "Rock"
m3 = "Scissor"

d1 = "Player Wins"
d2 = "Computer Wins"
d3 = "Draw"

i = 0
while i < 10:
    print("Press 1(Play) or 0(Stop)")
    print ("Options : ")
    print ("1 :", m1)
    print ("2 :", m2)
    print ("3 :", m3)
    print("Press |1|2|3| : ", end="")
    move = int(input())
    
    if move == 0:
        print("Game Stopped.")
        break
    
    if move == 1:
        print("Player : ", m1)
    elif move == 2:
        print("Player : ", m2)
    else:
        print("Player : ", m3)

    num = random.randint(1, 3)
    if num == 1:
        print("Computer : ", m1)
    elif num == 2:
        print("Computer : ", m2)
    else:
        print("Computer : ", m3)

    print("***---", end="")

    if move == 1 and num == 2:
        print(d1, end="")
    elif move == 1 and num == 3:
        print(d2, end="")
    elif move == 2 and num == 3:
        print(d1, end="")
    elif move == 2 and num == 1:
        print(d2, end="")
    elif move == 3 and num == 2:
        print(d1, end="")
    elif move == 3 and num == 1:
        print(d2, end="")
    else:
        print(d3, end="")

    print("---***")

    i += 1
