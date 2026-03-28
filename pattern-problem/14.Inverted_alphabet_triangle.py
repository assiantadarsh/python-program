# A B C D 
# A B C 
# A B 
# A 
# print the pattern


a = int(input("Enter the value of n:"))

for i in range(1,a+1):
    for k in range(0,a-i+1):
        d = 65 + k
        print(chr(d),end=" ")    # Type casting chr(d)
    print()