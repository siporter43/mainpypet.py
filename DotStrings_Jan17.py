from datetime import datetime

from datetime import timedelta

# Exercises
# ---------
# 1. get the current date and time and assign it to a variable now then print it
# 2. get a datetime object for your birthday and print it


def date_now():
    now = datetime.today()
    print(now)


date_now()

def birth():
    hbd = datetime(20001, 10, 7)
    print(hbd)

birth()


# Exercises
# ---------
# 1. Print just the date of the current datetime object using the .date() method
# 2. Print just the time of the current datetime object using the .time() method
# 3. Print a sentence like:
#    The year of our lord YEAR, on the DAY day of the MONTHth month, something happened!
#    (Using the .year, .day, and .month properties.)


now = datetime.today()
print(now.date())
print(now.time())

print(f"This is the year of the year of {now.year},on the {now.day} day of the {now.month}th month and I'm sure nothing will happen")


# Exercises
# ---------
# 1. import timedelta type from the datetime module
# 2. make a timedelta for a year
# 3. multiply a year by ten to make a decade

year = timedelta(days = 365)
decade =  year * 10
century = decade * 10

# Exercises
# ---------
# 1. Find out the date a week from now
# 2. Look up the date of the last solar eclipse. Print how many days it has been since then.
#    Bonus: Use timedelta objects to calculate how many years, months, and days it has been.

time = now + timedelta(weeks = 1)
print(f"Next week will be {time}")

solar_eclipse = datetime(2021, 12, 4)
dif_eclipse= now - solar_eclipse
dif_eclipse_wk= dif_eclipse / timedelta(weeks=1)
print(f"It has been {int(dif_eclipse_wk)} weeks since our last eclipse")
