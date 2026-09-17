a=input('Enter password : ') 
b=a[0:4] 
c=a[4:8]
if len(a)!=8:
    print('Invalid')
elif b.isalpha()==False:
    print('Invalid')
elif c.isdigit()==False:
    print('Invalid')
else:     
    print('Valid') 