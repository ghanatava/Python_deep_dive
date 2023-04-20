#generator that returns a sequence from x to y

def gen(x,y):

    while x<y:
        yield x
        x+=1

g=gen(5,10)
for i in g:
    print(i)

def char_gen():
    yield 'A'
    yield 'B'
    yield 'C'

g1=char_gen()
for i in g1:
    print(i)

