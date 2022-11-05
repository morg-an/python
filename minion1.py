import math

def solve(num):
    #Initialize variables
    low = 0
    guess = 500
    high = 1000
    count = 0
    answer = []
    remainder = num

    #Loop for as long as there is more than 0 left to use.
    while(count < 1000 and remainder > 0):

        #Print for testing purposes only.
        print("Loop: ", count+1)
        # print("Remainder: ", remainder)
        print("Guess: ", guess)
        # print("Area: ", guess*guess)
        print("Answer: ", answer)
        print("")

        #Square my guess and compare to remaining area. If there is not enough surface, set guess as the new 'high' value and calculate new guess (using math.floor to round guess down)
        if(guess*guess > remainder):
            high = guess
            next_guess = math.floor((low+high)/2)
            count += 1
            if guess == next_guess:
                answer.append(guess*guess)
                print(answer)
                remainder = remainder-(guess*guess)
                high = remainder
                low = 0
                guess = next_guess
                count = 0
            elif guess != next_guess:
                guess = next_guess
            else:
                print("Whoops")

        #Raise guess if it's too low.
        elif(guess*guess < remainder):
            low = guess
            next_guess = math.floor((low+high)/2)
            count +=1
            if guess == next_guess:
                answer.append(guess*guess)
                remainder = remainder-(guess*guess)
                high = remainder
                low = 0
                guess = next_guess
                count = 0
            elif guess != next_guess:
                guess = next_guess
            else:
                print("Whoopsie")
   
        #Ends the loop and returns answer when the last value is found.
        else:
            answer.append(guess*guess)
            remainder = remainder-(guess*guess)
            return answer
    answer

print(solve(129803))