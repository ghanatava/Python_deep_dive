class Employee:
    
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary

    def display(self):
        print(self.name)
        print(self.salary)


class Appraisal:
    @staticmethod
    def increment(e):
        e.salary+=10000
        e.display()


emp=Employee('Ashura',790000)
Appraisal.increment(emp)
