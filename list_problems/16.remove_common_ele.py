n = int(input("Enter the size of the list : "))

# Que -> Remove Common Elements from Two Lists .

arr = []

m = int(input("Enter the size of the second list : "))

if(n <= 0 or m <= 0):
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

common = []

for i in range(n):
    for j in range(m):
        if(arr[i] == arr2[j]):
            common.append(arr[i])
            
print("Common Elements list is :",common)  

unique = []

for i in arr:
    if i not in common:
        unique.append(i)

for j in arr2:
    if j not in common:
        unique.append(j)
        
print("Final result is : ",unique)