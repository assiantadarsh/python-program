n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to separate even and odd numbers from a list into two different lists.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

arr_even = []
arr_odd = []

for i in range(n):
    if(arr[i] % 2 == 0):
        arr_even.append(arr[i])
    else:
        arr_odd.append(arr[i])
        
print("Even number list is : ",arr_even)
print(f'Odd number list is : {arr_odd}')