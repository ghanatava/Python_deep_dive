import re
str='an apple a day keeps the doctor away'
result=re.findall(r'\ba[\w]*\b',str) #all words starting with a '[\w]*' represents 0 or more alphanumeric char

for i in result:
    print(i)

#all words starting with a digit
str1 = 'Ore no 1chiban daisuki wa ore da !'
result = re.findall(r'\d[\w]*', str1)
for i in result:
    print(i)

