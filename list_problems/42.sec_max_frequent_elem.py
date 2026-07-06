n = int(input("Enter n : "))

arr = []

for i in range(n):
    
    value = int(input())
    arr.append(value)

max_count = float('-inf')
sec_max = float('-inf')

max_value = 0
sec_value = 0

for i in range(n):
    
    visited = False
    count = 0

    for j in range(0, i):
        
        if arr[i] == arr[j]:
            visited = True

    if visited == True:
        continue

    for k in range(0, n):
        
        if arr[i] == arr[k]:
            count += 1

    if max_count < count:
        
        sec_max = max_count
        sec_value = max_value

        max_count = count
        max_value = arr[i]

    elif sec_max < count and max_count != count:
        
        sec_max = count
        sec_value = arr[i]

if sec_max == float('-inf'):
    print("Second most frequent element is not found")
    
else:
    print("Second most frequent element is :", sec_value)