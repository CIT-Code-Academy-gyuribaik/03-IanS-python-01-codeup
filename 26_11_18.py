#홀짝 구분하기
a = int(input())
if a % 2==0:
    print (a,"is even")
else:
    print (a,"is odd")
#문자열 돌리기
str = input()
for i in range(len(str) ):
    print(str[i])
#n 번째 원소부터
def solution(num_list, n):
      return num_list[n-1:]
#문자열 정수의 합
def solution(num_str):
    sum=0    
    for n in num_str:
        sum=int(sum)+int(n)
    return sum    
#문자열의 앞의 n글자
def solution(my_string, n):
    return my_string[:n]
#글자 이어 붙여 문자열 만들기
def solution(my_string, index_list):
    a=""
    for n in index_list:
        a=a+str(my_string[n])    
    return 
#배열의 원소만큼 추가하기
def solution(arr):
    a=[]
    for n in arr:
        for f in range(n): 
            a.append(n)
    return a    
#if we use two for loops,we can use direct ways and the range ways 
