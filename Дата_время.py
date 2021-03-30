from datetime import datetime, date, time

today = date.today()
print(today)
print("{}.{}.{}".format(today.day,
today.month, today.year))

current_time = time()
print(current_time)

current_time = time(16, 25)
print(current_time)

now = datetime.now()
print(now)

print("{}.{}.{}  {}:{}".format(now.day, now.month,
now.year, now.hour, now.minute))

print(now.date())
print(now.time())