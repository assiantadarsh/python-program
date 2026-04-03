# *
#   *       
#     *     
#       *   
#         * 
n = int(input("Enter rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

