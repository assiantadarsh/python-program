#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 
# print the triangle


def fact(n):
    factorial = 1
    for i in range(2,n+1):
        factorial = factorial*i
    return factorial

def combination(x,y):
    return fact(x)/(fact(y)*fact(x-y))
a = int(input("Enter the value of n:"))

for i in range(0,a):
    for j in range (a,i+1,-1):
        print(" ", end="")
    for k in range(0,i+1):
        print(int(combination(i,k)),end =" ")
    print()