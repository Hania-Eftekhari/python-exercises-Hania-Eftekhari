record=0
for i in range(1,11):
    h=float(input('enter jump height : '))
    if h > record:
        record = h
        print('highest record has been submitted!')
    else:
        print('this record was submitted before.')
        