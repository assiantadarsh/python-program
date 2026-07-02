class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        
    def display(self):
        print("Brand : ",self.brand)
        print("Model : ",self.model)
        print("Price : ",self.price)
        
c = car('mahindra ', 2022,3400000)  
c.display()