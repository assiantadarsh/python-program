n = int(input("Enter the size of the list : "))

# Que -> Count Even Numbers

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

count = 0
for i in range(n):
    if(arr[i]%2 == 0):
        count = count+1

print("The count of even number is : ",count)