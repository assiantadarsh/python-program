n = int(input("Enter the size of the list : "))

# Que -> Count Positive and Negative Numbers

if(n <= 0):
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter values : "))
    arr.append(value)

print("The list is : ",arr)

counte = 0
counto = 0
for i in range(n):
    if(arr[i] >= 0):
        counte +=1
    else:
        counto +=1
        
print(f"Positive count on the list is : {counte}")
print(f'Odd count on the list is : {counto}')