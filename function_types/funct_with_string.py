def count_vowle(text):
    
    count = 0
    
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
            
    return count

s = count_vowle("Adarsh Shukla")
print(f'Count : {s}')
