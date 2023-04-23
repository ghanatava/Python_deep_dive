
class Student:

    #mutator method
    def setName(self,name):
        self.name=name
    
    #accessor method
    def getName(self):
        return self.name
    

#create instances
n=int(input('No of students\n'))
i=0
while i<n:
    s=Student()
    s.setName(name=input('Enter name'))
    print(s.getName())
    print('---------------------------')
    i+=1




