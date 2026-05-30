n = int(input("Enter the size of the list : "))

if(n <= 0):
    print("Not possible")
    exit()

arr = []
for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

sum = 0

for i in range(n):
    sum += arr[i]

print("The total sum is : ",sum)
