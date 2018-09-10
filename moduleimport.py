import datetime
year, month, day = map(int,input().split(' '))
date1 = datetime.date(year, month, day)
adddays = datetime.timedelta(int(input()))
date2 = date1 + adddays
print(date2.year,date2.month,date2.day)