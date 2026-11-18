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
