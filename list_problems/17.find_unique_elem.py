n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to print only unique element from a list. If only one element is unique

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)
xor = 0

for i in range(n):
    xor = xor ^ arr[i]
    
print("The unique element is : ",xor)
