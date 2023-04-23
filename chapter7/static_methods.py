#understanding static methods
'''
    static methods are when processing is done on class level but does not require the class or instances involvement
'''

class Myclass:
    n=0
    def __init__(self) -> None:
        Myclass.n+=1

    #static method
    @staticmethod
    def noObjects():
        print('Number of objects',Myclass.n)

obj1=Myclass()
obj2=Myclass()
obj3=Myclass()

obj2.noObjects()
obj4=Myclass()
Myclass.noObjects()

#calculating square root 
import math
class SquareRoot:
    @staticmethod
    def sqrt(n):
        return math.sqrt(n)
    
n=4
result=SquareRoot.sqrt(n)
print(result)