n = int(input("Enter the size of the array : "))

# Que -> Move All Negative Numbers to the End

arr = []

for i in range(n):
    value = int(input("Enter value "))
    arr.append(value)
    
ans = []
    
i = 0

while(i < n):
    
    if(arr[i] >= 0):
        ans.append(arr[i])
    i += 1
    
j = 0

while(j < n):
    if(arr[j] < 0):
        ans.append(arr[j])
        
    j += 1
        
        
print(f'Ans : {ans}')