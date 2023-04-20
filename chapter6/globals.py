a=1
def func():
    a=2
    x=globals()['a']
    print('global=',x)
    print('local=',a)

func()