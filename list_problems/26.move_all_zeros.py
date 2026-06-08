n = int(input("Enter the size of the list : "))

# Que -> Move all zeros to the end of the list without changing the order of non-zero elements.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

i = 0
j = 1

while(i < n and j < n):
    
    if(arr[i] == 0 and arr[j] != 0):
        
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
        i += 1
        j += 1
        
    elif(arr[i] == 0 and arr[j] == 0):
        j += 1
        
    else:
        i += 1
        j += 1
        
print("After moving zeros the list is : ",arr)