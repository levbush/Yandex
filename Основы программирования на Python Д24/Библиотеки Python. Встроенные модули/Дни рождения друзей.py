from datetime import timedelta, date
now = date.today()
taget_date = now + timedelta(days=int(input()))
print(taget_date.day, taget_date.month)