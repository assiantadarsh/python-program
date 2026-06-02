n = int(input("Enter the size of the list : "))

# Que -> Merge Two Lists

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

m = int(input("Enter the size of the second list : "))


if(m <= 0):
    print("Not possible")
    exit()

arr2 = []

for i in range(m):
    value = int(input("Enter values : "))
    arr2.append(value)

print("The list is : ",arr)
print("The list is : ",arr2)

# Merge two lists

merge = arr + arr2
print(f"Merged list is : {merge}")

# OR
arr.extend(arr2)
print(f"Merged list is : {arr}")
    