import math

def solution(area):
    #Initialize variables
    low = 0
    guess = 500
    high = 1000
    answer = []
    remainder = area

    #Loop for as long as there is more than 0 left to use.
    while(remainder >= 1):

        #Square my guess and compare to remaining area. If there is not enough surface, set guess as the new 'high' value and calculate new guess (using math.floor to round guess down)
        if(guess*guess > remainder):
            high = guess
            guess = math.floor((low+high)/2)

        #if square of guess is less than remainder and a new guess would not be higher, add the square area to solution list
        elif(guess*guess < remainder):
            low = guess
            next_guess = math.floor((low+high)/2)
            if guess == next_guess:
                answer.append(guess*guess)
                remainder = remainder-(guess*guess)
                high = remainder
                low = 0
                guess = next_guess
            #Raise guess if it's too low
            elif guess != next_guess:
                guess = next_guess
   
        #Ends the loop and returns answer when the last value is found.
        else:
            answer.append(guess*guess)
            return answer

    #Tacks on the remainder if starting number contained a decimal.
    if remainder > 0:
        answer.append(remainder)
    
    return answer

print(solution(15324.5))