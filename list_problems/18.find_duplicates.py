n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to find duplicate elements in a list.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

temp = []

for i in range(n):
    isvisited = False
    
    for k in range(0,i):
        if(arr[i] == arr[k]):
            isvisited = True
    
    if(isvisited): continue
    else:
        for j in range(i+1,n):
            if(arr[i] == arr[j]):
                temp.append(arr[i])
        
print(f'The duplicated list is : {temp}')