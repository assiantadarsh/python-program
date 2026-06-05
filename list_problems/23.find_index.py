n = int(input("Enter the size of the list : "))

# Que -> Find the index position of a given element in a list.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

b = int(input("Enter element : "))

for i in range(n):
    if(arr[i] == b):
        print(f'The index is : {i}')
        exit()
        
print(f'The given element is not exist in the data')
