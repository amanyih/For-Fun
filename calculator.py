num1 = int(input("enter first number: "))
num2 = int(input("second number: "))
operation = input("enter operation")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/" and num2 != 0:
    print(num1/num2)
else:
    print("error")
