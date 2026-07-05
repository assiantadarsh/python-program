n = int(input("Enter the size of the array : "))

arr = []

for i in range(n):
    value = int(input(f'Enter {i + 1} elements : '))
    arr.append(value)

result = []

for i in range(n):
    
    visited = False
    
    for k in range(0 , i):
        if arr[i] == arr[k]:
            visited = True
            break
        
    if(visited):
        continue
    else:
        for j in range(i+1 ,n):
            if(arr[i] == arr[j]):
                result.append(arr[i])
                break
            
print(f'All Repeating element is : {result}')
