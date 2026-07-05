n = int(input("Enter n : "))

# Que -> Find the Element with Minimum Frequency .
arr = []

for i in range(n):
    value = int(input())
    arr.append(value)
    
min_count = float('inf')
value = 0

for i in range(n):
    visited = False
    count = 0
    
    for j in range(0, i):
        if arr[i] == arr[j]:
            visited = True
    
    if visited == True:
        continue
    
    else:
        for k in range(0,n):
            if arr[i] == arr[k]:
                count += 1
                
        if(min_count > count):
            min_count = count
            value = arr[i]
            
print(f'Minimum frequency element is : {value}')
