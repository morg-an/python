from datetime import datetime

#setting a date and time
birthday = datetime(1990, 2, 16)
print(birthday.year)
print(birthday.month)
print(birthday.day)

#finding weekday of a date time
print(birthday.weekday())

#setting current datetime
current_time = datetime.now()

#add and subtract datetimes
print("Since the beginning of the year, it has been: ", current_time-datetime(2022, 1, 1))

#parsing a date using datetime
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
user_entered_date = "January 15, 2018"
parsed_date = datetime.strptime(user_entered_date, '%B %d, %Y')
print(parsed_date)

#rendering a date as a string
parsed_date_string = datetime.strftime(parsed_date, '%B %d, %Y')
print(parsed_date_string)