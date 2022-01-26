letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#create dictionary by zipping together letters and points
letters_to_points = dict(zip(letters,points))

#add blank tile to the dictionary
letters_to_points[" "] = 0

#create a function to score a word
def score_word(word):
  #set initial score to 0
  score = 0
  #make word uppercase to match dictionary
  uppercase_word = word.upper()
  #iterate through each letter in the word
  for letter in uppercase_word:
    score += letters_to_points.get(letter, 0)
  #return score
  return(score)

#test scrabble calculator
word = "BROWNIE"
word_score = score_word(word)
print("The word " + word + " scores " + str(word_score) + " points.")

#score a full scrabble game
#Create dictionary with all players and their word choices
player_to_words = {"player1":["blue", "tennis", "exit"], "wordNerd":["earth", "eyes", "machine"], "Lexi Con":["Eraser", "Belly", "Husky"], "Prof Reader":["Zap", "Coma", "Period"]}

#define empty dictionary to store scores for each player
player_to_points = {}
#iterate through players
for player in player_to_words:
  #start each player at 0 points
  player_points = 0
  #iterate through each player's word choices
  for word in player_to_words.get(player):
    #add each word score to each player's score
    player_points += score_word(word)
  #add player and score to player_to_points dict
  player_to_points[player] = player_points

#display all player's scores
print(player_to_points)