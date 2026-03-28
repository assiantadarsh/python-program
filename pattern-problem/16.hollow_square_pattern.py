# *****
# *   *
# *   *
# *   *
# *****
# print the pattern

a = int(input("Enter the positive value of a:"))

for i in range (1,a+1):
    for j in range (1,a+1):
        if(i == 1 or i == a or j == 1 or j== a):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
    