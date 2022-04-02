import random
print('=========================Task11.2=================')
a = random.randint(1,6)
b= random.randint(1,6)
while True:
    h=1
    while h <=3:

        user= input('if uh want to play game press yes or no')
        if user == 'yes':
            pass
        elif user == 'no':
            break
        print(a,b)
        if a==b:
            print('you won')
            break
        else:
            print('you failed')
            h =h+1