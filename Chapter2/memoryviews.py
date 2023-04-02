#handling six bytes of memory as 1x6,2x3 and 3x2 views

from array import array
octets=array('B',range(6))
m1=memoryview(octets)
print(m1)
print(m1.tolist())
m2=m1.cast('B',[2,3])
print(m2.tolist())
m3=m1.cast('B',[3,2]) # WARNING!can also convert types to corrupt data
print(m3.tolist())
print(octets)

#using memoryviews to corrupt
num=array('h',[-2,-1,0,1,2])
memv=memoryview(num)
memv_oct=memv.cast('B')
print(memv_oct.tolist())
memv_oct[5]=4 #corruption
print(num)