# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 0
# print the pattern
a = int(input("enter positive number :"))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()