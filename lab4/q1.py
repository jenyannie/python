import calendar
from datetime import date, datetime 

current_date = date.today()
current_time = datetime.now().time()
day_of_the_month = current_date.strftime("%d")
day_of_the_year = current_date.strftime("%j")


print("current date: ",current_date)
print("current time: ",current_time)
print("current year: ",current_date.year)
print("month of the year: ",current_date.month)
print("week number of the year: ",current_date.isocalendar()[1])
print("weekday of the week: ",current_date.weekday())
print("day of the year: ",day_of_the_year)
print("day of the month: ",day_of_the_month)
print("day of the week: ",calendar.day_name[current_date.weekday()])