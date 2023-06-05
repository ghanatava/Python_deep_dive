from threading import *

l1=Lock()
l2=Lock()

def book():
    l1.acquire()
    print('Book locked train')
    print('Book wants to lock on compartment')
    l2.acquire()
    print('Book locked compartment')
    l2.release()
    l1.release()
    print('booked')

def cancel():
    l2.acquire()
    print('cancel locked compartment')
    print('cancel wants to lock on train')
    l1.acquire()
    print('cancel locked on train')
    l1.release()
    l2.release()
    print('Cancelled')

t1=Thread(target=book)
t2=Thread(target=cancel)

t1.start()
t2.start()