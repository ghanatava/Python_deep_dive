str=input('Enter a string')
sub=input('enter substring')

i=0
flag=False
n=len(str)

while i<n:
    pos=str.find(sub,i,n)
    
    if pos!=-1:
        print('found at=',pos)
        i=pos+1
        flag=True
    else:
        i=i+1

if flag==False:
    print('not found')
        


# Formatting 
id,name,email=1,'ashura','theashura@example.com'
str='{},{},{}'.format(id,name,email)
print(str)


#Fstrings

str=f'{name}-{id}-{email}'
print(str)