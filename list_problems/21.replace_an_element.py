n = int(input("Enter the size of the list: "))

# Que -> Replace an Element in a List

if n <= 0:
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter value: "))
    arr.append(value)

print("The list is:", arr)

b = int(input("Enter element which you want to replace: "))
c = int(input("Enter new element: "))

found = False

for i in range(n):
    if arr[i] == b:
        arr[i] = c
        found = True

if found:
    print("After replacing:", arr)
else:
    print("The given number was not found")