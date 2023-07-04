# date time lib in python

import datetime

# construct time in python only time without date
my_time = datetime.time(2,20,1,20)
print(my_time)
print(my_time.hour)
print(my_time.minute)

# construct date in python only date without time
today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)


today_db_format = today.ctime()
print(today_db_format)

from datetime import datetime

my_date_time = datetime(2021,10,3,14,20,1)
print(my_date_time) #-> 2021-10-03 14:20:01
my_date_time = my_date_time.replace(year=2023)
print(my_date_time)
print()

# date comparison 
date_time_one = datetime(2023,10,3,11,30,12)
date_time_two = datetime(2021,10,3,14,20,1)

diffrent = date_time_one-date_time_two

print(type(diffrent)) # <class 'datetime.timedelta'>
print(diffrent)
print(f"total days diffrent :{diffrent.days}")
print(f"total diffrent second:{diffrent.seconds}")
print(f"all total diffrent time in second : {diffrent.total_seconds()}")