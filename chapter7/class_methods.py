class Bird:
    
    wings=2

    @classmethod
    def fly(cls,name):
        print(f'{name} flies with {cls.wings} wings')

Bird.fly('Sparrow')

#lets test if instance can modify it
b=Bird()

b.wings=3
b.fly('Sparrow')
Bird.fly('Sparrow')
# result it can not