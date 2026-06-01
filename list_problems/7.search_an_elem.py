n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to check whether a given element exists in a list or not.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

target = int(input("Enter the target : "))

for i in range(n):
    if arr[i] == target:
        print("Element are present")
        exit()

print("Not present")