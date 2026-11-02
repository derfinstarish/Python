# get year, month, day from user and find the user age by using datetime module

import datetime

year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

BirthDate = datetime.date(year, month, day)
CurrentDay = datetime.date.today()
Age = CurrentDay.year - BirthDate.year

if (CurrentDay.month, CurrentDay.day) < (BirthDate.month, BirthDate.day):
	Age -= 1
print(f"You are {Age} years old.")