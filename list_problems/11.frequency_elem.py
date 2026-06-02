n = int(input("Enter the size of the array : "))

# Que -> Find frequency of each element 

if(n <= 0):
    print("Not possible")
    exit()
    
arr = []

for i in range(n):
    value = int(input("Enter value : "))
    arr.append(value)

print(f'The list is {arr}')

for i in range(n):
    isvisited = False
    count = 0
    
    for k in range(i):
        if(arr[k] == arr[i]):
            isvisited = True
            break
            
    if(isvisited == True): continue
    else:
        for j in range(n):
            if(arr[i] == arr[j]):
                count += 1
                
        print(f"{arr[i]} appears {count} time")
    