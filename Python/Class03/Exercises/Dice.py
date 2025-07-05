import random

i = 0
while i < 100:
    num = int(input("Enter any number (0 to quit): "))
    
    if i % 2 == 0:
        print("Player1 : ")
    else:
        print("Player2 : ")
    
    if num == 0:
        break

    arr = []
    cnt = 0

    while True:
        ludorDan = random.randint(1, 6)
        arr.append(ludorDan)
        print("Rolled:", ludorDan)
        
        if ludorDan != 6 or cnt == 2:
            break
        cnt += 1
    
    print("Final Rolls:", arr)
    i += 1
