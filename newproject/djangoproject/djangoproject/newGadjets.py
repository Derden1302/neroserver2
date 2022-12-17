from datetime import datetime, timedelta, time

periodD = { 1 : 60, 2 : 30, 3:1440}
rangeD={24 : 1 ,3 : 3,7 : 7}

start_date = datetime.today() + timedelta(minutes=1440)
end_date = datetime.today()
print(start_date)
