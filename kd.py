# def gcd(num,num2):
#     counter,fact = 1,1
#     finalfac = min(num,num2)
#     while counter<=finalfac:
#         if (num % counter == 0) and num2 % counter == 0:
#             fact = counter
#         counter += 1
#     print(fact)

# gcd(12,18)

# def num_digits(num):
#     counter = 0
#     while num != 0:
#         num = num // 10
#         counter +=1
#     print(counter)

# num_digits(1)

# def big_v(num):
#     space = " "
#     for i in range(num-1,-1,-1):
#         print((num-i)*space+"\\"+2*(i*space)+"/")

def dna(dna):
    for i in dna:
        if i == "A":
            print("T",end="")
        elif i == "T":
            print("A",end="")
        elif i == "C":
            print("G",end="")
        else:
            print("C",end="")

dna("ACAAGATGCCA")
        
        

