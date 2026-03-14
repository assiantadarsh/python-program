# *  *  *  *  
# *  *  *  *  
# *  *  *  *  
# *  *  *  *  
# print the pattern

a = int(input("enter positive number :"))

for i in range(1,a+1):
    for j in range(1,a+1):
        print("*  ",end="")
    print()