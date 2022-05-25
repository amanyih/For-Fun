def multi(x,y):
    z = y
    if x!=0 and y !=0:
        for i in range(x-1):
            y+= z
        print(y)
    else:
        print(0)
multi(4,5)