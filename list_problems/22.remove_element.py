n = int(input("Enter the size of the list : "))

# Que -> Remove a given element with another element in a list.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

b = int(input("Enter element to remove : "))

arr2 = []

found = False

for i in range(n):
    if(arr[i] == b):
        found = True
        
    else:
        arr2.append(arr[i])

if(found):
    print("The new array is : ",arr2)
else:
    print("The given element is not found")