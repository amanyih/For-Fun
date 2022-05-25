def weird(*n):
    sum = 0
    for i in n:
        sum += int(i)
    print("max:",max(n))
    print("min:",min(n))
    print("sum:",sum)
    print("avg:",sum/len(n))
weird(45,545,32,13)

num = input("nn: ")
num = num.split(",")
weird (num)