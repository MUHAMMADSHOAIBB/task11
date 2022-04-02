import random
print('===================TAsk 11.1=====================')
colorhex =['shoaib','ahmed','ali,' 'hammad',5,6,7,8,2,84,]
print(random.choices(colorhex))
# random alphabetical string
import string
alphabets = 26
print(random.choices(string.ascii_letters,k =alphabets))
#random value betweem two integers
integers = random.randint(1,40)
print("random value between two integers is",integers)
#multiple of 7
multiple = random.randrange(7,70,7)
print(multiple,"is a multiple of 7")
