n = int(input("Enter the size of the list : "))

# Que -> Write a Python program to print all elements that are greater than the average of the list.

if(n <= 1):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

# Find Average

sum = 0
for i in range(n):
    sum += arr[i]
    
average = sum / n

temp = []

for i in range(n):
    if(average < arr[i]):
        temp.append(arr[i])
        
print(f'Answer is : {temp}')