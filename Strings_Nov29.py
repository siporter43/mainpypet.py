# Here is where we will do some string, list, and method work

# 1. Make a list of seasons (lowercase). Print the first three characters of the 3rd season, title cased.
# 2. Make a dictionary where the key is the numbers 1-7 and the value is the days of the 
#       week: monday - sunday.
#    - Write a function that takes one argument, a number, and returns the day of the week 
#       associated with that number.
# 3. Make a dictionary named schedule where the key is a weekday and the value is another dictionary. 
#    - The inner dictionary should be the schedule for the day, where the key is the time in 
#       24 hour format (ie: "14:30")
#      and the value is the thing scheduled
#    - Use a for loop to iterate over each day and print the day name,
#    - then use a nested for loop to iterate over the schedule and print the time and activity

# Imports

from pathlib import Path

# Global Variables

seasons = ["autumn", "winter", "spring", "summer"]

week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

schedule = {
    "Monday": {
        "12:30": "Dance Off",
        "15:30": "Nap",
        "15:31": "Power Nap",
        "15:33": "Sleep Walk to Library"
    },
    "Tuesday": {
        "10:30": "Boom"
    },
    "Wednesday":{
        "11:00": "Elevensies",
        "13:00": "Late Lunch"
    }
}
# FNCNS

def find_day(day):
    print(week[day])

# Runner

print(format(seasons[2], ".3s").capitalize())

find_day(8)
