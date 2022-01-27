#Objective: Write a game where the player has to guess a random number between 1-1000 in as few turns as possible.
#Use the console to print messages and take input from the player.
#Have a 2 option menu for the player to start a new game or exit at the start.
#Once playing, loop through starting new games until the player chooses to exit.

import random

print("To play this game, choose the correct number between 1 and 1000 in as few guesses as possible. Ready to play?")
print("Type [1] to play [2] to exit")
#Loop to continue giving players the option to play
while True:
    #get selection of whether or not to play from user
    selection = input()
    #validate that the player made a vaid selection
    while selection not in ("1", "2"):
        print("You didn't follow instructions. Type [1] to play [2] to exit")
        selection = input()
        print("New selection", selection)
    #If user wants to play:
    while selection == "1":
        print("Let's play")
        #set a counter to keep track of the number of turns
        guess_count = 0
        #generate the random number for the game
        correct_number = random.randint(1, 1000)
        #print("Correct Number: ", correct_number)
        #set guess to false so that the following loop repeats until the user gets the correct answer
        guess = False
        while guess == False:
            #get the player's next guess
            print("What number do you want to guess?")
            guessed_number = input()
            #display the most recent guess
            print("You guessed:", guessed_number)
            #increase the score counter for every additional guess
            guess_count += 1
            #determine if the guess is high, low, or correct
            if guessed_number.isdigit():
                if int(guessed_number) < correct_number:
                    print("Your guess was too low. Try again.")
                elif int(guessed_number) > correct_number:
                    print("Your guess was too high. Try again.")
                elif int(guessed_number) == correct_number:
                    guess = True
                    print("You won in " + str(guess_count) + " turns!")
            #gives an error and restarts the loop if the user entered something other than a number. 
            else:
                print("Try again. You must enter a whole number between 1 and 1000")
                #reduces the score counter by 1 because the guess wasn't valid and I'm a nice person.
                guess_count -= 1
        print("Play again? Press [1] to play and [2] to exit")
        selection = input()
    #ends the game when the user says they don't want to play.
    if selection == "2":
        print("Bye")
        break