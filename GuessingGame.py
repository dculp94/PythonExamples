import random

print('Hello, What is your name?')
name =input()

secretNumber = random.randint(1,20)
print('Well, ' +name+ ' , guess a number between 1 and 20')
try:
 for guessesTaken in range (0,6,1):
    
    print('You have ' +str(6-guessesTaken)+ ' guesses to guess the number I am thinking of')
    guess = int(input())
    
    if guess < secretNumber:
        print ('Your guess is too low')
        
    elif guess > secretNumber:
        print ('Your guess is too high')
        
    
    else:
        break
except ValueError:
        'Enter a number only'   
        
if guess == secretNumber:
    print('Awesome, ' +name+ ' you found out the number in ' + str(guessesTaken+1)+ ' times')

else:
    print('Try again bud, maybe next time')
          
