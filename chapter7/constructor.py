class Student:

    def __init__(self,name,marks) -> None:
        self.name=name
        self.marks=marks

    def display(self):
        print('Hi ',self.name)
        print('you scored',self.marks)

s=Student('karna',100)
s.display()
        