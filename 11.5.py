import random
print('==================task 11.5===================')
while True:
   print('hello welcome to OMG game')
   user = input('Do  you want to play OMG game or exit')
   if user == "play":
       pass
   elif user == 'exit':
       break
   print('which game you want to play,\nplease select your option')
   choice = int(input('1 .who are uh,2. want to know the colour of  personality,3.'
                  'know the meaning of  name'))
   if choice==1:
       character= ['thief','hero','modern','good person','lawer','bussinessman','politician']
       print('You are a ',random.choices(character))
   elif choice ==2:
       colour =['black','White','Black and white','Normal']
       print('Your colour is',random.choices(colour))
   elif choice ==3:
       name = ['star','sun','lion','beautiful','coward','strong']
       print('The meaning of your name is',random.choices(name))