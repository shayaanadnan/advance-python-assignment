from datetime import datetime

def find_day(date_string):
    date_format = datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_format.weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]    
    return days[day_of_week]
date_string = '2024-02-10'
print(find_day(date_string))  
