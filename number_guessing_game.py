 #Let build the logic if 
# first of all let suppose a number variable assume a 
# then int type casting
# choose a random module random.ranint()


# for(i = 0; i < n; i++){if (a = 23): print("The number guess is correct") while(a != 23) so that it sjhows higher than guessing. if(a > 23) print('too high") elif: th enumber is low else: th enumber is not found.  try: excepterror: if wrong invalid input other than 100}

    
import random 

print("Number guessing game")

print("I have selected a number between 1 and 100.")

#generate a random number

number = random.randint(1, 100)

#attempt counter
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid whole number.")
         
        