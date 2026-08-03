a=float(input('enter purchase amount : '))
if a > 1000000:
   print(a-(0.15*a))    
elif 500000 < a < 1000000:
     print(a-(0.10*a))
elif a < 500000:
     print(a)
     
    