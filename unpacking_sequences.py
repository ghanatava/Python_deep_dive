#parallel assignment

lax_coordinates=(33.9425,-118.408056)
latitude,longitude=lax_coordinates
print(latitude)
print(longitude)

#prefixing with x

t=(20,8)
quotient,remainder=divmod(*t)
print(quotient)

print(remainder)

import os 
_,filename=os.path.split('/home/ashura/Desktop/python_dive/tupples.py')
print(filename)

# Using * to grab excess items

a,*body,c,d=range(5)  #* can come at any position 
print(a,body,c,d)

#using * to define lists and other sequencies
tup=*range(4),4
print(tup)
lst=[*range(5),5]
print(lst)
Set={*range(4),5,*range(6,9)}
print(Set)