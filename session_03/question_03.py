sum=0
for i in range(1,11):
    if i%2!=0:
        i*5
        sum=sum+(i*5)
    elif i%2==0:
        i+5
        sum=sum+(i+5)
print(sum)