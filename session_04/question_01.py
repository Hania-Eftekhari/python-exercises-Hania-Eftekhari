import random
number=random.randint(1,51)
while True:
    a=int(input('Enter a number on a scale from 1 to 50 : ')) 
    if a>number:
        print('You have entered a larger number, try again.') 
    elif a<number:
        print('You have entered a smaller number, try again.')
    elif a==number:
        print('Congratulations! you hove choosen the correct number.') 
        break