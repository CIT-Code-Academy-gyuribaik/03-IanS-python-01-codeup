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

#삼각형의 완성조건 (1)
def solution(sides):
    sides.sort()
    if sides[2]<sides[0]+sides[1]:
        return 1
    else:
        return 2

#모음 제거
def solution(my_string):
    vowels=["a","e","i","o","u"]
    for v in vowels:
        my_string=my_string.replace(v,"")
    return my_string    

#대문자와 소문자
def solution(my_string):
      a=""     
      for i in range(len(my_string)):
       if my_string[i].islower():
          a= a+my_string[i].upper()
       else: 
          a= a+my_string[i].lower() 
      return a     
