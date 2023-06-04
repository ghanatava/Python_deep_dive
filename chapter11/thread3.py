# Creating threads without subclassing to Thread

from threading import *


class MyThread:
    def __init__(self,str):
        self.str=str
    
    def display(self,x,y):
        print(self.str)
        print(f'args are {x} and {y}')


obj = MyThread('Hello')
t1=Thread(target=obj.display,args=('Threading','Cool',))
t1.start()