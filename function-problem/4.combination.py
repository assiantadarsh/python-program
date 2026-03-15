def combination(x):
    fact = 1
    for i in range (2,x+1):
        fact = fact * i
    return fact

def factorial(n,r):
    return combination(n) / (combination(r) * combination(n-r))
    

n = int(input("Enter n :"))
r = int(input("Enter r :"))

if(n<0 or r<0):
    print("The combination is not possible for negative number")

elif(n == 0 and r == 0):
    print("Combination = 1")

else:
    print("Combination = ",int(factorial(n,r)))
