# creating a list using list comp.
symbols='$#%*@~`'
codes=[ord(symbol) for symbol in symbols]  #ord() returns the unicode alues of the characters
print(codes)

#making a listcomp variable global using the walrus operator

x="abc"
code2=[ord(char) for char in x ]
print(code2)

code2=[last := ord(c) for c in x]
print(code2)
print(last)

#cartesian product using list comprehension

colors=['black','green','yellow','red']
sizes=['S','M','L','XL','XXl']

tshirts=[(color,size) for color in colors for size in sizes]
print(tshirts)
