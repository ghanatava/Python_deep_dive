class Person:
    def __init__(self) -> None:
        self.name='Charles'
        self.db=self.Dob()

    class Dob:
        def __init__(self) -> None:
            self.dd=10
            self.mm=4
            self.yy=2004

        def display(self):
            print(f'Dob={self.dd}/{self.mm}/{self.yy}')

    def display(self):
        print(f'Name={self.name}')

p=Person()
p.display()
x=p.db
x.display()

