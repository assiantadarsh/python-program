n = int(input("Enter n : "))

arr = []

for i in range(n):
    value = int(input("Enter value : "))
    arr.append(value)

# Bubble sort
for i in range(n - 1):
    flag = False

    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            flag = True
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if flag == False:
        break

count = 1
max_count = 1

for i in range(1, n):
    if arr[i] == arr[i - 1] + 1:
        count += 1

        if count > max_count:
            max_count = count

    elif arr[i] == arr[i - 1]:
        continue

    else:
        count = 1

print("Sorted list :", arr)
print(f"Longest consecutive sequence length is : {max_count}")