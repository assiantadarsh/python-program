# ques -> Count constant in a string ?

s = input("Enter s : ")

constant = 0

s = s.lower()
for ch in s:
    if (ch == 'a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == ' '):
        continue
    
    else:
        constant += 1
        
print(f'constant : {constant}')