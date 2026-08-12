# Calculator
a = float(input("Enter a 1st number"))
b = float(input("Enter a 2nd number"))
op = input("Enter operater(+,-,*,/,%,**):")

if op  == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
elif op == '%':
    print(a % b)
elif op == '**':
    print(a ** b)
else:
    print("INVALID OPERATER!!!")    