class Sample:

    # a class variable
    x=10

    #a class method
    @classmethod
    def modify(cls):
        cls.x+=1

s1=Sample()
s2=Sample()

s1.modify()
print(s1.x)
print(s2.x)