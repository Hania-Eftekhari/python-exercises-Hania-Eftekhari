import random
a=['rock', 'paper', 'scissors'] 
while True:
    b=input('Enter rock, paper or scissors, and enter exit to end the game : ')
    c=random.choice(a) 
    print(c)
    if b=='exit':
        print('The game is over.') 
        break
    elif b not in a:
            print('Invalid input')
            continue
    if c==b:
        print('same choices! try again.') 
    elif b=='rock' and c=='scissors':
        print('You won!')
    elif b=='paper' and c=='rock':
        print('You won!') 
    elif b=='scissors' and c=='paper':
        print('You won!') 
    else:
            print('Computer won!') 
            