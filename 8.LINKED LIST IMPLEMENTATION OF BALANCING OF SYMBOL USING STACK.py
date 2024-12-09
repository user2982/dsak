def check(s):
    stack = []
    
    for char in s:
        if char in ["{", "[", "("]:  
            sta
            if not stack: 
                return False
            val = stack.pop()  
            if val == "(": 
                if char != ")":
                    return False
            elif val == "{": 
                if char != "}":
                    return False
            elif val == "[": 
                if char != "]":
                    return False
    
    if stack:  
        return False
    
    return True

n = int(input())
for i in range(n):
    s = input() 
    if check(s):
        print("Balanced")
    else:
        print("Not Balanced")
