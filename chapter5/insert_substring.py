str=input('Enter a string: ')
sub=input('Enter a sub string')

n=int(input('Enter position index'))

l1=len(str)
l2=len(sub)

str1=[]
for i in range(n):
    str1.append(str[i])

#appending substring

for i in range(n,l2):
    str1.append(sub[i])

#appending rest of character from str

for i in range(n+1,l1):
    str1.append(str[i])

str1=''.join(str1)
print(str1)
