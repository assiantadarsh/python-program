n = int(input("Enter the size of the list: "))

# Que -> Find the third largest element in a list.

if n <= 0:
    print("Not possible")
    exit()

arr = []

for i in range(n):
    value = int(input("Enter value: "))
    arr.append(value)

print("The list is:", arr)

first_max = float('-inf')
sec_max = float('-inf')
third_max = float('-inf')

for i in range(n):
    if first_max < arr[i]:
        third_max = sec_max
        sec_max = first_max
        first_max = arr[i]

    elif sec_max < arr[i] and arr[i] != first_max:
        third_max = sec_max
        sec_max = arr[i]

    elif third_max < arr[i] and arr[i] != first_max and arr[i] != sec_max:
        third_max = arr[i]

if third_max == float('-inf'):
    print("Third maximum element does not exist")
else:
    print(f"The third maximum element is: {third_max}")