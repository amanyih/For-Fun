from math import factorial


def facorial(num):
    multiple = 1
    for i in range(1,num+1):
        multiple = multiple * i

    print(multiple)

facorial(3)