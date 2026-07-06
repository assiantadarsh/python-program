n = int(input('Enter n : '))

# Que -> Write a Python program to find the element that appears more than n/2 times in a list.

arr = []
frequency = False
Value = 0

for i in range(n):
    Value = int(input("Enter value : "))
    arr.append(Value)
    
print(arr)

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
                
    if count > n / 2:
        frequency = True
        Value = arr[i]
        break
        
if(frequency):
    print(f'Majority element is : {Value}')
else:
    print('Majority elements is not found')
    