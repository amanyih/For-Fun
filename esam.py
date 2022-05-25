# user = int(input("enter a number: "))
# def fac(num):
#     mul = 1
#     for i in range(num,0,-1):
#         mul = mul * i
#     print(mul)

# fac (user)

# def mul(a,b):
#     c = b
#     for i in range(a-1):
#         b = b + c
#     print(b)
# mul(9,5)

# def dadd(num):
#     num = str(num)
#     sum = 0
#     for i in num:
#         sum = sum + int(i)
#     print(sum)
# dadd(576)

# def fac_add(num):
#     x = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             x = x + i
#     print(x)
# fac_add(8)

def prime(num):
    x = 0
    for i in range(1,num):
        if num % i ==  0:
            x = x + i
    if x == 1:
        print("prime")
    if x > 1:
        print("composite")

prime(14)