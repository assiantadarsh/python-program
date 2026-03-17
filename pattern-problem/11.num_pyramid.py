#    1
#   222
#  33333
# 4444444
# print the pattern

a = int(input("enter positive num.:"))
nse = 2

for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end="")
    for k in range(1,nse):
        print(i,end="")
    nse +=2
    print()
    