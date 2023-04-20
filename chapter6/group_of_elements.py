#function to find total and average

def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum+=i
        avg=sum/n
        return sum,avg
    
print('enter elements separated by space:')
lst=[int(x) for x in input().split()]

x,y=calculate(lst)
print('Total=',x)
print('Average=',y)

#display group of string
def display(lst):
    for i in lst:
        print(i)

print('enter strings separated by space:')
lst=[x for x in input().split()]
display(lst)
