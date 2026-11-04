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

#1:for a in num_list= directly putting a into the num_list variable (doing the equations/act right onto the variable a.)
#2:for i in range(len(num_list))=using indexes to find out the number (doing the equation/act onto the index.) 
                                #1.range(3) index 0,1,2
                                # 2.range(1,5) index 1,2,3,4           
                                # 3.range(1,10,2) index 1,3,5,7,9
                                    
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

#각도기
def solution(angle):
    if angle<90:
        return 1
    elif angle==90:
        return 2
    elif 90<angle<180:
        return 3
    else:
        return 4
