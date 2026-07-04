n = int(input("Enter the size of the array : "))

arr = []

for i in range(n):
    value = int(input(f'Enter {i + 1} elements : '))
    arr.append(value)
    
flag = False

for i in range(i):
    for j in range(i + 1 , n):
        if arr[i] == arr[j]:
            flag = True
            break
        
    if(flag):
        print("First repeating element is :",arr[i])
        break