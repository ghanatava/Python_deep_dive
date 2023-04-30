''' A class containing only the abstract methods is called interface'''
from abc import *
class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print('Connecting to oracle db')

    def disconnect(self):
        print('Disonnecting from oracle db')

class Sybase(Myclass):
    def connect(self):
        print('Connecting to Sybase')

    def disconnect(self):
        print('Disonnecting from Sybase db')

class Database(Myclass):
    str=input('Enter database name ')
    #convert string to class name
    str=str.strip()
    classname=globals()[str]

    x=classname()

    x.connect()
    x.disconnect()

