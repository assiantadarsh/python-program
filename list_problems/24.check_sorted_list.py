n = int(input("Enter the size of the list : "))

# Que -> check whether a list is sorted in ascending order or not.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

for i in range(0,n-1):
    if(arr[i] > arr[i+1]):
        print("The given list is not sorted")
        exit()
        
print("The list is sorted")