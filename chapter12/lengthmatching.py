# find all 5 letter words
import re
str1 = 'Ore no 1chiban daisuki wa ore da'
result = re.findall(r'\b\w{7}\b', str1)
for i in result:
    print(i)

# all words with atleast 4 chars
result = re.findall(r'\b\w{4,}\b', str1)
print(result)

# retrieve last word if it starts with t
# the \A is for beginning and \z is for last

result = re.findall(r'd[\w]*\Z', str1)
print(result)
