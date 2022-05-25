def gcd(a,b):
    for i in range(a,1,-1):
        if (a % i) == 0 and (b % i) == 0:
            print (i)
            break
gcd(12,18)