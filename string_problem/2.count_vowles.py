# ques -> Count vowles in a string ?

s = input("Enter s : ")

vowles = 0

s = s.lower()
for ch in s:
    if (ch == 'a' or ch =='e' or ch == 'i' or ch == 'o' or ch == 'u'):
        vowles += 1
        
print(f'Vowles : {vowles}')