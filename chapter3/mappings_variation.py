#collections.ChainMap
from collections import ChainMap,Counter

d1=dict(a=1,b=3)
d2=dict(a=2,b=4,c=6)

chain=ChainMap(d1,d2)
print(chain['a'])
print(chain['c'])

#collections.Counter
ct=Counter('abracadabra')
print(ct)
print(ct.most_common(3))



