def ramanujan(num):
    sum = 0
    rang = int(num**(1/3))
    for a in range(1,rang):
        for b in range(1,rang):
            for c in range(1,rang):
                for d in range(1,rang):
                    if a!=b and a != c and a != d and b != c and b != d and c != d:
                        if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                            sum = a ** 3 + b ** 3
                            print(a,b,c,d," -- ",sum)

ramanujan(10000)





