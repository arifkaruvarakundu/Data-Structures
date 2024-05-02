def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
        
    return list(duplicates)

lst = [1,2,3,3,4,1,6,7,8,9,6]

dp = find_duplicates(lst)
print(dp)

####################################################

def find_duplicates(lst):
    count_item = {}
    duplicates = []
    
    for item in lst:
        if item in count_item:
            count_item[item]+=1
            if count_item[item]==2:
                duplicates.append(item)
            
        else:
            count_item[item] =1 
            
    return duplicates