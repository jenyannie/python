import datetime

current_date = datetime.date.today()
new_date = current_date - datetime.timedelta(5)
print("current date: ",current_date)
print("5 days before current date is: ",new_date)