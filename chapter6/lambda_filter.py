# lambda that returns even numbers

lst=[x for x in range(10)]
print(lst)
lst1=list(filter(lambda x:(x%2==0),lst))
print(lst1)

#lambda with map function to return squares
lst=[1,2,3,4,5]
print(lst)
lst1=list(map(lambda x:x**2,lst))
print(lst1)

#lambda with reduce function
from functools import *
lst=[1,2,3,4,5]
print(lst)
result=reduce(lambda x,y:x*y,lst)
print(result)