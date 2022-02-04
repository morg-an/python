# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum = 0
  values = my_dictionary.values()
  for value in values:
    sum += value
  return sum

#testing
print(sum_values({"milk":5, "eggs":2, "flour": 3})) # Answer: 10
print(sum_values({10:1, 100:2, 1000:3})) # Answer: 6

# Create a function called sum_even_keys that takes a dictionary named my_dictionary, 
# with all integer keys and values, as a parameter. 
# This function should return the sum of the values of all even keys.

def sum_even_keys(my_directory):
  sum = 0
  for key in my_directory:
    if key % 2 == 0:
      sum+=my_directory.get(key)
  return sum

#testing
print(sum_even_keys({1:5, 2:2, 3:3})) # Answer 2
print(sum_even_keys({10:1, 100:2, 1000:3})) # Answer: 6

# Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
# The function should add 10 to every value in my_dictionary and return my_dictionary

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] = my_dictionary[key] + 10
  return my_dictionary

#testing
print(add_ten({1:5, 2:2, 3:3})) # Answer {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3})) # Answer {10:11, 100:12, 1000:13}

# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
# This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
  values_that_are_keys = []
  for key in my_dictionary.keys():
    for value in my_dictionary.values():
      if key == value:
        values_that_are_keys.append(key)
  return values_that_are_keys

#testing
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10})) # Answer [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100})) # Answer ['a']

# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
# The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  largest_value = float("-inf")
  highest_key = float("-inf")
  keys = list(my_dictionary.keys())
  values = list(my_dictionary.values())
  for value in values:
    if value > largest_value:
      largest_value = value
      highest_key = keys[values.index(value)]
  return highest_key

# testing
print(max_key({1:100, 2:1, 3:4, 4:10})) # Answer 1
print(max_key({"a":100, "b":10, "c":1000})) # Answer 'c'