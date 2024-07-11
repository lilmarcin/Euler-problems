def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def count_sundays():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 0 - Monday
    # 1 - Tuesday
    # ...
    # 6 - Sunday
    day_of_week = 1 # 1 Jan 1901 was on Tuesday
    sundays = 0  
      
    for year in range(1901, 2001):
        for month in range(12):
            if day_of_week == 6:
                sundays += 1
            day_of_week = (day_of_week + days_in_month[month]) % 7
            if month == 1 and is_leap_year(year):
                day_of_week = (day_of_week + 1) % 7
    return sundays
            

result = count_sundays()
print(result)