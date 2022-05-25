def ceil(num):
    mul = num * 10
    remin = mul % 10
    if remin == 0:
        return num
    else:
        return((mul-remin)//10) +1

print(ceil(3.7))