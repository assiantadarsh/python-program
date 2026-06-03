n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to find common elements between two lists

arr = []

m = int(input("Enter the size of the second list : "))

if(n <= 0 | m <= 0):
    print("Not possible")
    exit()

print("Enter values of First array ")

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

arr2 = []

print("Enter values of second array ")

for i in range(m):
    value = int(input("Enter values : "))
    arr2.append(value)

print("The list is : ",arr)
print("The second list : ",arr2)

temp = []

for i in range(n):
    for j in range(m):
        if(arr[i] == arr2[j]):
            temp.append(arr[i])
            
print("Common Elements list is :",temp)          
                