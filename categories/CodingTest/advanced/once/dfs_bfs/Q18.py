# 괄호 변환

from collections import deque 

input_1 = "(()())()"
input_2 = ")("
input_3 = "()))((()"

def balanced_bracket_index(p):
    
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
        
def is_proper_bracket_set(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            
            if count == 0 :
                return False
            count -= 1
    return True
    

def solution(p):
    answer = ""
    
    if p == "":
        return answer
    
    index = balanced_bracket_index(p)
    
    u = p[:index+1]
    v = p[index+1:]
    
    if is_proper_bracket_set(u):
        answer = u + solution(v)
        
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution(input_1), solution(input_2) ,solution(input_3))