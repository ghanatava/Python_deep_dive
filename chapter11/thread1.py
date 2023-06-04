from threading import *


def display(arg):
    print(f'hello {arg}')


for i in range(5):
    t = Thread(target=display,args=('Threads',))
    t.start()

# Creating threads by subclassing Thread class

class MyThread(Thread):
    #overriding the run method
    def run(self):
        for i in range(6):
            print(i)


t1 = MyThread()
t1.start()
# wait till thread completes execution
t1.join()