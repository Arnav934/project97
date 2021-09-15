#Specific Tasks to complete the Project: 
#1. Create a guessingGame.py file. 
#2. Import a random module into your file. 
#3. Use random to generate a random number from 1-9. 
#4. Give users 5 chances to guess the number. 
#5. If the user guesses incorrectly, show a hint or message to the user if their guess was close or far. 
#6. If the user guesses correctly show the congratulating message. 
#7. Save the code. 8. Run and test the c

import random
number = random.randint(1,9)
chances = 0
print('guess a number between 1-9 ')
while chances < 5: 
    guessNumber = int(input('enter your guess: '))
    chances = chances + 1
    if guessNumber == number:
        print('YOU WON!!!')
        break
    elif not chances < 5:
        print('YOU LOSE! The number is: ', number)


