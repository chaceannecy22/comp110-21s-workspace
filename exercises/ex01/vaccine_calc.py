"""A vaccination calculator."""

__author__ = "730421780"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vac: int = int(input("Target percent vaccinated: "))

people_left: float = .01 * population * target_percent_vac - (doses_administered / 2)


daysx = people_left / (doses_per_day / 2)


today: datetime = datetime.today()
num_of_days_until_desired_vac: timedelta = timedelta(daysx)

day_of_desired_vac: datetime = today + num_of_days_until_desired_vac

print("We will reach " + str(target_percent_vac) + "% vaccination in " + str(round(daysx)) + " days,")
print("which falls on " + str(day_of_desired_vac.strftime("%B %d, %Y")) + ".")