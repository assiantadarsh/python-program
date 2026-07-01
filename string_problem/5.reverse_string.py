# Que -> Write a program to reverse a given string.

s = input("Enter string : ")

n = len(s) - 1

for i in range(n , -1, -1):
    print(s[i],end="")