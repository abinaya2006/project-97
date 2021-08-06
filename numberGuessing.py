import random
number =random.randint(0,10)

print("NUMBER GUESSING GAME")
print("Guess a number (between 0 and 10)")

numberOfGuesses=5

while numberOfGuesses>0:
    guess=int(input("Enter your guess:  "))
    numberOfGuesses=numberOfGuesses-1

    if(numberOfGuesses==0):
        print('YOU LOSE 😞 😞')
        print("The correct number is" ,number)
        print("Better luck next time 👍 👍")
        
    elif(guess<number):
        print("Your guess was too low : Guess a number higher than ", guess)
    
    elif(guess>number):
        print("Your guess was too high : Guess a number lower than ", guess)
    
    elif(guess==number):
        print("Congratulation YOU WON!! 🎊 🎊 ")
        break

    
    