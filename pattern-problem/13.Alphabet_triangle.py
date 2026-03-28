# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
# print the pattern

a = int(input("Enter the value of n:"))

for i in range(1,a+1):
    for k in range(1,i+1):
        d = 64 + k
        print(chr(d),end=" ")    # Type casting chr(d)
    print()