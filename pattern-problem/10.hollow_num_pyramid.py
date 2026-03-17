#     1
#    2 2
#   3   3
#  4     4
# 555555555
# print the pattern

a = int(input("enter positive num.:"))
nsp = 2
for i in range(1,a+1):
    if i ==a:
        for i in range(1,2*i):
            print(a,end="")
    else:
        for j in range(a,i,-1):
            print(" ",end="")
        for k in range(1,nsp):
            if k==1 or k==nsp-1:
                print(i,end="")
            else:
                print(" ",end="")
        nsp+=2
    print()
    