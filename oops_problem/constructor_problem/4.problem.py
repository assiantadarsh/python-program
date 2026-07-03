# Create a class Product with a constructor that takes product_name, price, and quantity. Find and print total bill amount.

class product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display(self):
        print("=====================================")
        print("Product_name : ",self.name)
        print("Price : ",self.price)
        print("Quantity : ",self.quantity)
        print("Total bill : ",self.price * self.quantity)
        print("========================================")
        
p = product('Oil',3400,12)
p.display()