n = int(input("Enter the size of the array : "))

# Que -> Rearrange List in Alternating Positive and Negative Order .

arr = []

for i in range(n):
    value = int(input())
    arr.append(value)
    
pos = []
neg = []
ans = []

for i in range(n):
    if arr[i] >= 0:
        pos.append(arr[i])
        
    else:
        neg.append(arr[i])
    
i = 0
j = 0

while(i < len(pos) or j < len(neg)):
    
    if(i < len(pos)):
        ans.append(pos[i])
        i += 1
    if( j < len(neg)):
        ans.append(neg[j])
        j += 1
     
print("Final ans : ",ans) 
  