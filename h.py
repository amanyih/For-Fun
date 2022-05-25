def lar(*num):
    for i in num:
        x = 0
        for j in num:
            if i<j:
                x+=1
        if (x == 0):
            print(i)

lar(2,3,8,5,7)
