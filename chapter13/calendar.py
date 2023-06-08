from calendar import *
yy=int(input('enter year: '))
mm=int(input('enter month'))

str1=month(yy,mm)
print(str1)

#printing calendar for entire year

print(calendar(2023,2,1,8,3))