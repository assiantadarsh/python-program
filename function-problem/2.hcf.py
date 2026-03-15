def hcf(a,b):
    x = 0
    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            x = i
    return x       
a = int(input("Enter positive num."))
b = int(input("Enter positive num."))

x = hcf(a,b)
print("HCF = ",x)