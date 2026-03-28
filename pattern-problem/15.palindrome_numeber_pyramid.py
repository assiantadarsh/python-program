#    1
#   121
#  12321
# 1234321
# print the pattern

a = int(input("Enter the positive value of a:"))

for i in range (1,a+1):
    for k in range (a,i,-1):
        print(" ", end="")
    for j in range (1,i+1):
        print(j,end="")
    for p in range(i,1,-1):
        print(p-1,end="")
    print()