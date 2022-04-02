import random
print('======================Task 11.4=================')
names = ['yasir','hamad','abdulmuhaimin','rehan','nazal','ali','farhan']
for x in names:
        h=0
        while h <=7:
         random.seed(h)
         score = random.randrange(60,90,5)
         print(x, "your score is",score)
         h =h+1
