n = int(input("Enter the size of the list : "))

# Que -> Find the Difference Between Maximum and Minimum Element .

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

max = float('-inf')
min = float('inf')

for i in range(n):
    if(max < arr[i]):
        max = arr[i]
    
    if(min > arr[i]):
        min = arr[i]
        
if max == float('-inf') or min == float('inf'):
    print(f'Difference is not possible')

else:
    print("Difference : ",max - min)
    