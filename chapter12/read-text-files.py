import re

with open('chapter12/mails.txt','r') as f:
    for line in f:
        res=re.findall(r'\S+@\S+',line)
        if len(res)>0:
            print(res)