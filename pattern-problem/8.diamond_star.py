#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# print the pattern

a = int(input("enter positive num.:"))

# For upper case 
for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end = "")
    for k in range(1,2 * i):
        print("*",end="")
    print()

# For lower case
nst = 2*a - 2

for i in range(1,a):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(1,nst):
        print("*",end="")
    nst -=2
    
    print()