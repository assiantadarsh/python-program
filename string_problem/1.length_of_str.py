# Ques -> Find length of string ?

a = str(input("Enter string : "))

# Method 1

print(f'Lenght = {len(a)}')

# Method 2
count = 0
for ch in a:
    count += 1
    
print(f'Lenght = {len(a)}')