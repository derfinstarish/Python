# get current date and time

# import datetime
# x = datetime.datetime.now()
# print(x)

# get current date

# import datetime
# z = datetime.date.today()
# print(z)

# attributes of datetime module

# import datetime
# print(dir(datetime))

# creting date objects

# import datetime
# x = datetime.datetime(2022,5,20)
# print(x)

# strftime() method

# import datetime
# x = datetime.datetime(2022,10,3)
# print(x.strftime("%b"))

# print today's year, month, day

# from datetime import date
# x = date.today()
# print("Current year:",x.year)
# print("Current month:",x.month)
# print("Current day:",x.day)

# accessing components of a datetime object

# from datetime import datetime
# dt = datetime.now()
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.minute)
# print(dt.second)
# print(dt.weekday)

# perform calculations with datetime objects (using timedelta)
# used to represent the difference between two dates or time - essentially a duration.

# from datetime import datetime,timedelta
# x = datetime.now() + timedelta(days = 7)
# print(x)

# y = datetime(2026, 8, 20, 12, 0, 0) - timedelta(hours = 2)
# print(y)

# add a delay using sleep

# import time
# print("hello")
# time.sleep(3)
# print("Hello Python")

# import datetime
# import time
# print(datetime.datetime.now())
# print(time.time())
# time.sleep(2)
# print("Program finished")

# fomatting datetime objects

# from datetime import datetime
# dt = datetime.now()
# x = dt.strftime("%y - %m - %d - %H : %M : %S")
# print(x)
# y = dt.strftime("%B %d, %Y")
# print(y)