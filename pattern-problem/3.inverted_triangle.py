# *  *  *  *  *  
# *  *  *  *  
# *  *  *  
# *  *  
# *  
# print the pattern 
a = int(input("enter positive number :"))

for i in range(a,0,-1):
    for j in range(i):
        print("*  ",end="")
    print()