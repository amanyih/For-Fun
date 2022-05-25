num = input("enter: ").split(",")
def fuck(a):
    sum = 0
    for i in a:
        sum = sum + int(i)
    print(sum/len(a))

fuck(num)
