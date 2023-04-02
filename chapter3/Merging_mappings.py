def dump(**kwargs):
    return kwargs


d=dump(**{'x':1},y=2,**{'z':3})
print(d)

# Using | and |= operators

d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d3 = d1 | d2      # | operator overrides the previous occurences with the latest ones and returns a new object
print(d3)


d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
d1 |= d2   # |= operator overrides the existing mappings inplace
print(d1)