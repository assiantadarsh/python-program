# a = c,b = a,c = b
def swap(a,b,c):
    a = a+b+c
    b = a-(b+c)
    c = a-(b+c)
    a = a-(b+c)
    return a,b,c
a = 5
b = 3
c = 1
x = swap(a,b,c)
print(x)
