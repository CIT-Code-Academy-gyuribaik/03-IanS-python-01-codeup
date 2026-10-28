#배열 원소의 길이
def solution(strlist):
    ans=[]
    for i in range(len(strlist)):
          ans.append(len(strlist[i]))  
    return ans           

#숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    a=0
    for i in range(len(my_string)):
       if my_string[i].isdigit():
            a=a+int(my_string[i])
    return a      

#모음 제거
def solution(my_string):
    vowels=["a","e","i","o","u"]
    for v in vowels:
        my_string=my_string.replace(v,"")
    return my_string    
