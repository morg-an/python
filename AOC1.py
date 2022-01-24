#One of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!
#Before you know it, you're inside a submarine the Elves keep ready for situations like this. 
# It has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough; 
#As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. 
# On a small screen, the sonar sweep report (your puzzle input) appears: 
# each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.
#This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.
#The first order of business is to figure out how quickly the depth increases - 
# you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

#Count the number of times a depth measurement increases from the previous measurement. 
#How many measurements are larger than the previous measurement?

list_of_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def count_depth_increases(list_of_depths):
    i = 1
    num_depth_increases = 0
    while i < len(list_of_depths):
        if list_of_depths[i] > list_of_depths[i-1]:
            num_depth_increases += 1
        i+=1
    return num_depth_increases

print(count_depth_increases(list_of_depths))