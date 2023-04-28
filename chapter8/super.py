class Square:
    def __init__(self,x):
        self.x=x

    def area(self):
        print('area=',self.x*self.x)

class Rectangle(Square):
    def __init__(self,x,y) -> None:
        super().__init__(x)
        self.y=y
    
    def area(self):
        super().area()
        print('area of rectangle =',self.x*self.y)

a,b=[float(x) for x in input('enter two measurements:').split()]
r=Rectangle(a,b)
r.area()
