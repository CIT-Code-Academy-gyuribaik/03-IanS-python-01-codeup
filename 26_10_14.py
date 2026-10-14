# 1. 짝수 홀수 개수 (1번 버전)
def solution(num_list):
    odd_count=0
    even_count=0    
    for a in num_list:
        if a%2==1 :
            odd_count +=1
        else:
            even_count +=1
    return [even_count,odd_count]    

# 2. 짝수 홀수 개수 (2번 버전)
def solution(num_list):
    odd_count=0
    even_count=0    
    for i in range(len(num_list)):
        if num_list[i]%2==1 :
            odd_count +=1
        else:
            even_count +=1
    return [even_count,odd_count]  
