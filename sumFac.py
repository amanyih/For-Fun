def sumfac(num):
    x = 0
    for i in range (1,num+1):
        if num%i == 0:
            x += i
    print(x)
sumfac(6)