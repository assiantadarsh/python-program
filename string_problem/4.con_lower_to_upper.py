# Convert lowercase later to upper case without using built in fn ??

s = input("Enter string : ")

ans = ""

for ch in s:
    if(ch >= 'a' and ch <= 'z'):
      ans += chr(ord(ch) - 32)
      
    else:
        ans += ch
print(ans)