#assignig function to a variable

def display(str):
    return 'HI '+str

a=display
print(a('Krishna'))

#function as a parameter to another function

def message():
    return 'How are U?'

print(display(message()))

#function returning another function

def display1():
    def message():
        return 'How are U?'
    
    return message

fun = display1()
print(fun())

    