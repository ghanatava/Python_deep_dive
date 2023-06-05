from threading import *
from time import *

class Theatre:
    def __init__(self,string) -> None:
        self.str=string
    
    def movieshow(self):
        for i in range(1,6):
            print(f'{self.str} : {i}')
            sleep(0.1)

obj1=Theatre('Cut Ticket')
obj2=Theatre('Show Seats')

t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)

t1.start()
t2.start()


    

