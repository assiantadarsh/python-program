a = int(input("enter num :"))
temp = a
rev = 0

while(a>0):
    rem = a % 10 
    rev = rev * 10 + rem
    a = a//10
if temp == rev:
    print("The given num is palindrome")
else:
    print("The given num is not palindrome")