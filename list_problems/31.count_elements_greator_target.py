n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to count how many elements in a list are greater than a given number.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

target = int(input("Enter target element : "))

count = 0

for i in range(n):
    if(target < arr[i]):
        count += 1
        
print("Number are greator then target : ",count)