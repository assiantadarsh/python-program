class laptop:
    
    def __init__(self):
        self.name =""
        self.ram = 0
        self.storage = 0
        
    def input(self):
        print("Enter the name of laptop : ")
        self.name = input()
        
        print("Enter the ram : ")
        self.ram = int(input())
        
        print("Enter the storage : ")
        self.storage = int(input())
        
    def display(self):
        print("Laptop name : ",self.name)
        if(self.ram >= 8):
            print("Laptop is used for coding")
            
        else:
            print("Laptop use for basic work only")
        
        print("Storage : ",self.storage)
        
l = laptop()
l.input()
l.display()