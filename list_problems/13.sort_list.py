n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to sort a list in ascending order without using the sort() function.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

# Use bubble sort

for i in range(n):
    flag = True
    for j in range(0 ,n - i- 1):
        if(arr[j] > arr[j+1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            flag = False
    if flag:
        break

print(f"Final Sorted list is : {arr}")    