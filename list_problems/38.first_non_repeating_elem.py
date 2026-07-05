n = int(input("Enter the size of the array : "))

arr = []

for i in range(n):
    value = int(input(f'Enter {i + 1} elements : '))
    arr.append(value)

for i in range(n):
    
    visited = False
    repeat = False
    
    for k in range(0 , i):
        if arr[i] == arr[k]:
            visited = True
            break
        
    if(visited):
        continue
    else:
        for j in range(i+1 ,n):
            if(arr[i] == arr[j]):
                repeat = True
                break
                
        if(repeat == False):
            print("First non repeating Element is : ",arr[i])
            break