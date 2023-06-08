from datetime import *
group=[]

group.append(date.today())
for i in range(1,11):
    next_date=date.today()+timedelta(days=i)
    group.append(next_date)

group.sort()
for i in group:
    print(i)

