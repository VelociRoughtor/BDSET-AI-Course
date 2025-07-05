# While loop
sum = 0
num = 0
i = 1
while i < 100:
    if i % 3 == 0:
        sum += i
        num += 1
    i += 1
avg = sum / num
print (avg)
