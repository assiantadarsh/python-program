n = int(input("Enter the size of the list : "))

# Que -> Smallest Element in a List.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

min = float('inf')
for i in range(n):
    if min > arr[i]:
        min = arr[i]

print("The minimum element is : ",min)