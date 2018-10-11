#! /usr/env/python

text = "yeah, but no, but yeah"

print(text == "yeah")
print(text.startswith("yeah"))
print(text.endswith("yeah"))
print(text.find("no"))

import re

date = "09/18/2018"

if re.match(r'\d+/\d+/\d+', date):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(date):
    print("yes")
else:
    print("No")

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

import random

values = [1,2,3,4,5,6]
random_values = random.shuffle(values)
print(values)

print(random.sample(values, 2))
print(random.choice(values))
print(random.sample(values, 4))

print(random.randint(0, 10))
print(random.random())
print(random.getrandbits(100))

from datetime import timedelta, datetime
print(timedelta(days=10, hours=10, seconds=60))
a = timedelta(days=10)
b = timedelta(seconds=10)
print(a + b)

print(datetime(2012, 9, 9))
a = datetime(2012, 9, 8)
b = timedelta(days=10)
print(a + b)

now = datetime.today()
print(now)
print(now + timedelta(hours=2))
print((datetime.now() + timedelta(days=6)).weekday())



# Get date for the given day's last occurance.

from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_day(given_day, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_target_num = weekdays.index(given_day)
    days_ago = ( 7 + day_num - day_target_num) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_day("Monday"))

from datetime import timedelta, date, datetime
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = datetime.today()
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return end_date
print(get_month_range())

text = "2012:09:01"
date_now = datetime.strptime(text, "%Y:%m:%d")
print(date_now)

from datetime import datetime
from pytz import timezone

today = datetime.today()
print(today)

