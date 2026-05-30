n = int(input("Enter the size of the list : "))

if(n <= 0):
    print("Not Possible")
    exit()

arr = []
for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("Your list is : ",arr)