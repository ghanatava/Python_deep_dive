l=[i for i in range(3)]
print(l)
print(id(l))
l*=2
print(l)
print(id(l))  #the id may or may not change depending upon whether __imul__ or __iadd__ methods are called or not for mutable sequence


t=tuple(i for i in range(3))
print(t)
print(id(t))
t*=2
print(t)
print(id(t)) #The id will change for immutable sequence as inplace mul (__imul__) can not be called


