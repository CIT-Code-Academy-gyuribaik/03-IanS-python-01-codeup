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


#문자 반복 출력하기
def solution(my, n):
    answer="" 
    for i in range(len(my)):
        answer+=my[i]*n    
    return answer

#문자 반복 출력하기(2)

def solution(my, n):
    answer="" 
    for i in my:
        answer+=i*n    
    return answer

#특정 문자 제거하기

def solution(my, letter):
    result = my.replace(letter,"")
    return result
