from abc import ABC,abstractmethod
import math

class Myclass(ABC):
    @abstractmethod
    def claculate(self,x):
        pass

#sub classes

class Square(Myclass):
    def claculate(self, x):
        print('Square=',x**2)

class Sqrt(Myclass):
    def claculate(self, x):
        print('Sqrt=',math.sqrt(x))

class Cube(Myclass):
    def claculate(self, x):
        print('Cube=',x**3)

#creating objects
obj1=Square()
obj2=Sqrt()
obj3=Cube()

obj1.claculate(4)
obj2.claculate(4)
obj3.claculate(4)