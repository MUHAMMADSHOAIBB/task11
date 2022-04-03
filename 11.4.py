import random
print('======================Task 11.4=================')
names = ['yasir','hamad','abdulmuhaimin','rehan','nazal','ali','farhan']
for x in names:
        random.seed(0)
        score = random.randint(60,90)
        print(x, "your score is",score)
