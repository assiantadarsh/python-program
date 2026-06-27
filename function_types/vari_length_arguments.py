def num(*number):   # *number is behave like tuple 
    
    total = 0
    
    for i in number:
        total += i
        
    print(f'Total Sum : {total}')
    
num(2,3,4,5,6,7,8,0,9)