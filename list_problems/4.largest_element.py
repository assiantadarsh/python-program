n = int(input("Enter the size of the list : "))

# Que -> 3. Largest Element in a List
if(n <= 0):
    print("Not Possible")
    exit()

arr = []
for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("Your list is : ",arr)

max = float('-inf')

for i in range(n):
    if(max < arr[i]):
        max = arr[i]

print("The maximum number is : ",max)