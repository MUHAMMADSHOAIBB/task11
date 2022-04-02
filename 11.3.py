import random
print('=================task 11.3====================')
int =[]
a=1
while a<=100:
    a=a+1
    number = random.randrange(1,100,1)
    print(int.append(number))
    for a in int:
        fre =int.count(a)
        print(a,"comes",fre,"times")