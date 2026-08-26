a=input('enter first colour : ')
b=input('enter second colour : ')
c=input('enter third colour : ')
if a==b and a==c and b==c:
    print('all colours are repetitive.')
elif a==b or a==c or b==c:
    print('two colours are repetitive.')
else:
    print('none of these colours are the same.')
    