def binary_conv(num):
    newnum = ''
    while(num>0):
        newnum = (str(num % 2)) + newnum
        num//=2
    return newnum

print(binary_conv(17))