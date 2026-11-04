#배열의 유사도
def solution(s1, s2):
    ans=0      
    for a in s2:
        if a in s1:
            ans=ans+1
    return ans
# we see if a(which is in s2) is in s1 and if it is we add one to the variable ans.  

#n의 배수 고르기
def solution(n, numlist):
    ans=[]
    for a in numlist:
        if a%n==0:
            ans.append(a)
    return ans    
# in arrangements we use append not addition

#자릿수 더하기
def solution(n):
    ans=0
    a=str(n)
    for i in a:
        ans=ans+int(i)
    return ans    
# int to str = number to sequence
