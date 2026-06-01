n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to remove duplicate elements from a list.
# method -> 2

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

temp = []

for value in arr:
    if value not in temp:
        temp.append(value)

print(temp)