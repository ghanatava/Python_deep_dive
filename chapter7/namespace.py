#understanding class namespace
class Student:
    x=10

#access class variable in class namespace
print(Student.x)
Student.x+=1
s1=Student()
s2=Student
#even classes can be passed to a variable(woww!)
s3=s2()
print(s3.x)
print(s1.x)

#understanding instance namespace

s1.x+=1
print(s1.x)
print(s2.x)