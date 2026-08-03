a=int(input('enter hour : '))
a==00 <= a <= 23
if  00 <= a <= 5:
    print('Midnight')
elif 6 <= a <= 11:
    print('Morning')
elif 12 <= a <= 14:
    print('Afternoon')
elif 15 <= a <= 18:
    print('Evening')
elif 19 <= a <= 23:
    print('Night')
elif a < 00 or a > 23:
    print('out of range.')