a=float(input('enter first number : '))
b=float(input('enter second number : '))
s=input('enter an operator : ')
if s=='+':
    print(a+b)
elif s=='-':
    print(a-b)
elif s=='*':
    print(a*b)
elif s=='/':
    print(a/b)
else:
    print('invalid operator')