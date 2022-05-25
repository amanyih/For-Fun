def digitsum(num):
    sum = 0
    x = num
    while x > 0:
        num = num % 10
        sum = sum + num
        x = x // 10
    print(sum)

digitsum(576)