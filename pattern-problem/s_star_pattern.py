# *   * * * 
# *
# * * * * * 
#         * 
# * * *   * 


n=int(input("Enter odd number: "))

for i in range(1,n+1):
    for j in range(1,n+1):

        if i==1 and j>=n//2+1:
            print("*",end=" ")

        elif j==1 and i<=n//2+1:
            print("*",end=" ")

        elif i==n//2+1:
            print("*",end=" ")

        elif j==n and i>=n//2+1:
            print("*",end=" ")

        elif i==n and j<=n//2+1:
            print("*",end=" ")

        else:
            print(" ",end=" ")

    print()

