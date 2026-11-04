#배열의 유사도
def solution(s1, s2):
    ans=0      
    for a in s2:
        if a in s1:
            ans=ans+1
    return ans
# we see if a(which is in s2) is in s1 and if it is we add one to the variable ans.  
