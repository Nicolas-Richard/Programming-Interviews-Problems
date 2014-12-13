#Write a function that, given a string (such as 'AABBCCCCCBABAA') returns
#the character with the longest consecutive substring. In this case, it is C, because
#there are 5 Cs in a row, which trump all other characters.

def longest_consecutive_substring(sentence):
    
    dict = {}
    
    previous_letter = sentence[0]
    
    dict[sentence[0]]=0
    
    count = 1
    
    for i in range(1,len(sentence)): 
                
        if sentence[i-1] == sentence[i]:
            
            count +=1  
            
        else:
            
            if count > dict[sentence[i-1]]:
                dict[sentence[i-1]] = count
                dict[sentence[i]] = 1
                count =1
        
    if count > dict[sentence[len(sentence)-1]]:
        
        dict[sentence[len(sentence)-1]] = count
                     
    max_counter = 0
    max_key = sentence[0]
   
    
    for key in dict.keys():
                
        if dict[key] > max_counter:
            max_key = key
    
    print dict
    return max_key        
    
    
test1 = 'AABB'
test2 = 'ABBBAB'
test3 = 'CCCA'
print longest_consecutive_substring(test3)        
        
        
        
            
        
        