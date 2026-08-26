a=input('Enter string : ')
if len(a)%2==0:
    for i in range(len(a)//2):
        print(a[i],end='')
elif len(a)%2!=0:
    for i in range(len(a)//2, len(a)):
        print(a[i],end='')
        