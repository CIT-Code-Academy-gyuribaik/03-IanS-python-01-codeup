#제곱수 판별하기
def solution(n):
    for a in range(n):
        if n==a*a:
            return 1
    return 2   
#if a(an iteger) squared is an integer we return 1 and else, a 2

#제곱수 판별하기
    def solution(n):
    if (n**(1/2))==int(n**(1/2)) :
        return 1
    else:
        return  2 if 
#if n squared is an integer we return 1

#세균 증식
def solution(n, t):
    return n*(2**t)세균 증식

#머쓱이보다 키 큰 사람
def solution(array, height):
    sum=0
    for x in array:
        if height < x:
           sum = sum+1
    return sum      

#옷가게 할인 받기
def solution(price):    
    if price>=500000:
        price=price*(0.8)
    elif price>=300000:
        price=price*(0.9)
    elif price>=100000:
        price=price*(0.95)  
    return int(price)    
#if you use more than one if they all get counted causing an invalid answer
#if you go from least to greatest they all get counted and it returns an invalid answer

#짝수는 싫어요
def solution(n):
    b=[]
    a=0
    for a in range (n+1):
        if a%2==1 and a<=n:
            b.append(a)  
    return b    
