x=10
print(x,id(x))

def modify(x):
    x=15
    print(x,id(x))

modify(x)
print(x)

#weird output in modified list
def modify_lst(lst):
    lst.append(9)
    print(lst,id(lst))

lst=[1,2,3,4]
modify_lst(lst)
print(lst,id(lst))