#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
# print the pattern

a = int(input("enter positive num.:"))

for i in range(1,a+1):
    for j in range(a,i,-1):
        print(" ",end = " ")
    for k in range(1,2 * i):
        print("*",end=" ")
    print()