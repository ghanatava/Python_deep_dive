from threading import *


class MyThread(Thread):
    
    def __init__(self,str):
        Thread.__init__(self)  # call Thread class constructor
        self.str=str
    #overriding the run method
    def run(self):
        print(self.str)



t1 = MyThread('Hello')
t1.start()
# wait till thread completes execution
t1.join()
