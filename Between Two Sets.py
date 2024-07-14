# https://www.hackerrank.com/contests/mountblue-technologies/challenges/between-two-sets
def getTotalX(a, b):
    # Write your code here
    
    count = 0
    
    for i in range(min(a), max(b)+1):
        
        fact = True 
        
        for j in a:
            if i % j !=0:
                fact = False
                break
        for j in b:
            if j % i !=0:
                fact = False            
                break
        
        if fact == True:
            count+=1
    return count