def dice():
    num = int(input("number of sides: "))
    import random
    result = random.randint(1,num)
    return result

print(dice())