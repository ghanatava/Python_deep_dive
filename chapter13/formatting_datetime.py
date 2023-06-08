from datetime import *
td=date.today()
print(td)

# format and convert to str
str1 = td.strftime("%d,%B,%Y")
print(str1)

tm=datetime.now()
print(tm)
print('Time:',tm.strftime("%H:%M:%S"))
