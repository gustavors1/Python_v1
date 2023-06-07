### Dates ###

# Date time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

# Time

from datetime import time 

current_time = time(21, 6, 59)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 31)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 2, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2024 - now
print(diff)

diff = year_2024.date() - current_date
print(diff)

# Timedelta

start_timedelta = timedelta(25, 560, 100, weeks = 12)
end_timedelta = timedelta(12, 100, 200, weeks= 62)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

