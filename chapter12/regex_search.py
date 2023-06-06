# a program to create regular expression and search for string starting with m and having 3 characters

import re

str1='man sun mop run'
result = re.search(r'm\w\w', str1)
#w represents any alpha-numeric, W represent any non alpha numeric

if result:
    print(result.group())

# to find all that matches

result=re.findall(r'm\w\w',str1)
if result:
    print(result)

str2='This; is the: "Core" Python\'s book'
result = re.split(r'\W+', str2)  # '+' indicate occurence of more than or equal to 1.
print(result)

# substituting a substring

res = re.sub(r'man', 'fuck', str1)
print(res)
