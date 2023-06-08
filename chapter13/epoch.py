# time since in epoch
import time
epoch=time.time()
print(epoch)#seconds since epoch January 1 of current year

t = time.localtime(epoch)
d = t.tm_mday
m = t.tm_mon
y = t.tm_year
h = t.tm_hour
mins = t.tm_min
s = t.tm_sec

print(f'{d}/{m}/{y} :: {h}:{mins}:{s}')

#alternate use ctime()
print(time.ctime(epoch))

