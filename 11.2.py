import random
print('=========================Task11.2=================')
chances=1
while chances <=3:

        dice = [1, 2, 3, 4, 5, 6]
        a = random.choices(dice, k=2)
        print(a,)
        if a[0]==a[1]:
            print('you won')
            break
        elif chances == 3:
            print('You Failed!')
            break
        else:
            print('you failed')
            h =chances+1
