symbols='$#%*@~`'

print (tuple(ord(s) for s in symbols))

import array

print(array.array('I',(ord(symbol) for symbol in symbols)))

#cartesian product in genexp

colors=['black','green','yellow','red']
sizes=['S','M','L','XL','XXl']

for tshirts in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirts)

