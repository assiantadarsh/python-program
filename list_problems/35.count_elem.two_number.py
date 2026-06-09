n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to count all elements from a list that are between two given numbers.

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

low = int(input("Enter first number : "))
high = int(input("Enter second number : "))

count = 0

for i in range(n):
    if(arr[i] > low and arr[i] < high):
        count += 1
        
print(f'{count} three number between {low} and {high}')