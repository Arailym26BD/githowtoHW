# 1 Write a Python program to subtract five days from current date.
import datetime as dt
print(dt.date.today()+dt.timedelta(-5))

# 2 Write a Python program to print yesterday, today, tomorrow.
from datetime import timedelta, date
print("Today: ", date.today())
print("Yesterday: ", date.today() - timedelta(days=1))
print("Tomorrow: ", date.today() + timedelta(days=1))

# 3 Write a Python program to drop microseconds from datetime.
from datetime import datetime, time, date

dateis = datetime.now()
print(dateis.year, dateis.month, dateis.day, dateis.hour, dateis.minute, dateis.second)


# 4 Write a Python program to calculate two date difference in seconds.
from datetime import datetime, timedelta, time

today = datetime.now()
newdate = today + timedelta(days = 16)

# differenceinseconds = (newdate - today).total_seconds()
differenceinseconds = (newdate - today).total_seconds()
print(differenceinseconds)
