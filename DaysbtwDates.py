from datetime import date # The 'date' class from the 'datetime' module is imported to work with dates.

f_date = date(2026, 6, 1)
l_date = date(2026, 6, 13)

diff = l_date - f_date
print(diff.days) # This will print the number of days between the two dates.