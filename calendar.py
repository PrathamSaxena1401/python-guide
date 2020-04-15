import calendar
print(calendar.weekheader(1))
#this will output M T W T F S S
print(calendar.firstweekday())
#this will print the index of the first week day ie monday ie 0

print(calendar.month(2020,4))
#this will print the whole month
print(calendar.monthcalendar(2020, 4))
#this will return the index of whole week days in this month
print(calendar.calendar(6000))
#this will print the whole freaking year
print(calendar.weekday(2020,4,14))
#print the index of the day on that date

print(calendar.isleap(2021))
#finds wether the year is leap or not

print(calendar.leapdays(2020,2026))
#how many leap days fall between