a=float(input('enter balance : '))
b=float(input('enter withdrawal amount : '))
if b<=0:
    print('invalid number.')
elif a>=b:
    print('the operation was successfully completed!')
elif a<b:
    print('your card balance is insufficient.')
