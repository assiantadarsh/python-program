n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to remove duplicate elements from a list.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

temp = []

for i in range(n):
    isvisited = False
    for k in range(i):
        if(arr[k] == arr[i]):
            isvisited = True
    if(isvisited == True) :continue
    else:
        temp.append(arr[i])   
        
print("After delete duplicates the list is : ",temp)