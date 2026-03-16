#     1
#    121
#   12321
#  1234321
# 123454321
# print the pattern

a = int(input("enter positive num.:"))

for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end = "")
    for k in range(1,i+1):
        print(k,end="")
    for p in range(i-1,0,-1):
        print(p,end="")
    print()