a = int(input("Enter first  number"))
b = int(input("Enter second number"))

for i in range(1 , 10001):
    if i % a == 0 and i % b == 0:
        print("First number divisible by both : " , i)
        break