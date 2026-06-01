n = int(input("Enter the size of the list : "))

# Que -> find the second largest element in a list.

if(n <= 1):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

max = float('-inf')
sec_max = float('-inf')

for i in range(n):
    if max < arr[i]:
        sec_max = max
        max = arr[i]
    
    elif sec_max < arr[i] and max != arr[i]:
        sec_max = arr[i]
        
if(sec_max == float('-inf')):
    print("The second maximum are not present")
else:
    print("The second maximum element is : ",sec_max)