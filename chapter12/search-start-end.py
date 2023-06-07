import re
str1='Hello world'
res=re.search(r"^He",str1)
if res:
    print('starts with He')
else:
    print('did not start from He ')

#finding a word at the end of a string

str2='Hello world'
res=re.search(r"world$",str2)
if res:
    print(f'found {res.group()}')
else:
    print('not found')

#searching case insensitively 
str3='Hello world'
res=re.search(r"World$",str3,re.IGNORECASE)
if res:
    print(f'found {res.group()}')
else:
    print('not found')
# retrieve timings either am or pm

str4='The time line is 8AM to 9AM and 2PM to 4PM'
res=re.findall(r'\dam|\dpm',str4,re.IGNORECASE)
print(res)