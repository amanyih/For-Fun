def big_v(num):
    space = " "
    for i in range(num-1,-1,-1):
        print((num-i)*space+"\\"+2*(i*space)+"/")

big_v(19)