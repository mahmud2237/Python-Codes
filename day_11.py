"""
seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365
days_per_leap_year = 366

#standard year math
seconds_per_year_standard = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_year
print(f"There are {seconds_per_year_standard} seconds in a standard year.")
#leap year math
seconds_per_year_leap = seconds_per_minute * minutes_per_hour * hours_per_day * days_per_leap_year
print(f"There are {seconds_per_year_leap} seconds in a Leap year.")

#ask user for days of a year
days_this_year = int(input("How many days are in this year?"))

if days_this_year == 366:
  print("Number of seconds in a leap year are", seconds_per_year_leap)
else:
  print("Number of seconds in a standard year are", seconds_per_year_standard)

"""

days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)
