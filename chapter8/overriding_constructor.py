class Father:
    def __init__(self):
        self.property=800000

    def display(self):
        print('Father\'s property=',self.property)

class Son(Father):
    def __init__(self):
        self.property=2000000

    def display(self):
        print('Child\s property=',self.property)

s=Son()
s.display()