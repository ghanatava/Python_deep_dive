import time
print(time.ctime())


from datetime import *

d=date(2016,4,29)
t=time(15,30)
dt=datetime.combine(d,t)
print(dt)
dt=dt.replace(year=2017, month=6, day=4, hour=16, minute=28, second=59)
print(dt)
