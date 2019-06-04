import datetime

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)

print(tday.year)
print(tday.day)
print(tday.weekday())    # Monday 0 Sunday 6
print(tday.isoweekday())  # Monday 1 Sunday 7

tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - tdelta)

# date 2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2019, 12, 23)
till_bday = bday - tday
print(till_bday)
print(till_bday.total_seconds())


t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)
