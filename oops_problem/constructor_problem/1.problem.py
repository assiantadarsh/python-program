class student:
    def __init__(self,name,roll_nu,course):
        self.name = name
        self.roll_nu = roll_nu
        self.course = course
        
    def display(self):
        print('Name :',self.name)
        print(f'roll num : {self.roll_nu}')
        print(f'course : {self.course}')
        
s = student("adarsh",23,"JAVA")
s.display()
    