def list_fun(number):
    
    max = number[0]
    
    for i in number:
        if(max < i):
            max = i
            
    print(f'Maximum number is : {max}')
    
list_fun([2,3,4,5,6,7])
