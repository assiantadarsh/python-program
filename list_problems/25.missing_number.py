n = int(input("Enter the size of the list : "))

# Que -> Find the missing number from a list containing numbers from 1 to n.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

xor1 = 0
for i in range(n):
    xor1 = xor1 ^ arr[i]
    
xor2 = 0

for i in range(1,n+2):
    xor2 = xor2 ^ i
    
print("The missing number is : ",xor2 ^ xor1)