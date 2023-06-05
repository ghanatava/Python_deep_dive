from threading import *
from time import *

class Railway:
    def __init__(self,available) -> None:
        self.available=available
        self.l=Lock()

    def reserve(self,wanted):
        self.l.acquire()
        print(f'avaialable numer of births {self.available}')

        if self.available>=wanted:
            name=current_thread().name
            print(f'Birth {wanted} is aloted for {name}')
            sleep(1.5)
            self.available-=wanted

        else:
            print('sorry no births left')

        self.l.release()

obj=Railway(1)

t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))

t1.name='First person'
t2.name='Second person'

t1.start()
t2.start()

