def permutation(x):
    fact = 1
    for i in range (2,x+1):
        fact = fact * i
    return fact

def factorial(n,r):
    return permutation(n) / permutation(n-r)
    

n = int(input("Enter n :"))
r = int(input("Enter r :"))

if(n<0 or r<0):
    print("The Permutation is not possible for negative number")

elif(n == 0 and r == 0):
    print("Permutation = 1")

else:
    print("Permutation = ",int(factorial(n,r)))
