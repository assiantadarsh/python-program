class circle:
    def __init__(self , radius):
        self.radius = radius
    
    def display(self):
        print("Area : ",3.14 * self.radius * self.radius)

r = int(input("Enter the radius : "))
        
c = circle(r)
c.display()
