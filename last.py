def larD(a,b):
    y=0
    lar = 0
    for i in range(a,b):
        x = 0
        for j in range (1,i+1):
            if i % j == 0:
                x+=1
        if x > y:
            y = x
            lar = i
    print("number of factors",y)
    print("number:",lar)    
larD(7,10)    