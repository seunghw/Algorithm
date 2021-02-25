def solution(strings, n):
    answer = []
    n_answer = [] 		
    
    for string in strings:	
        n_answer.append(string[n])
    
    n_answer.sort()			
    
    for i in n_answer:		
        for string in strings:
            if string[n] == i:
                answer.append(string)	
          
    return answer