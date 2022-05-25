for i in range (1,1000):
    for j in range (2,i+1):
        x = 0
        if i%j == 0:
            x +=1

print(x)