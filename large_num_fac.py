def larfac(num):
    y = 0
    for i in range(1,num):
        x = 0
        for j in range(1,i):
            if i%j == 0:
                x+=1
        if x > y:
            y = x
            z = i
    print("it's",z,'with',y,"factors")

larfac(1000)
        