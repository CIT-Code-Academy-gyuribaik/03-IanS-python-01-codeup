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
