class student:
    def __init__(self,name,roll_nu,classes,school):
        self.name = name
        self.roll_nu = roll_nu
        self.classes = classes
        self.school =  school
        
    def display(self):
        print("==============================")
        print("Name : ",self.name)
        print(f'Roll num : {self.roll_nu}')
        print(f'Class : {self.classes}')
        print(f'School : {self.school}')
        print("===============================")
    
s = student("Adarsh Shukla",2344,12,"SPUMV")

s.display()