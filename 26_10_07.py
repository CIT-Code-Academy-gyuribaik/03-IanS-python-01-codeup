#숫자 비교하기
def solution(num1, num2):
    if num1==num2:
        return 1
    else:
        return -1
#나이 출력
def solution(age):
    return 2023-age
#몫 구하기
def solution(num1, num2):
    return num1//num2
#피자 나눠 먹기 (3)
def solution(slice, n):
    if n%slice==0:
        return n/slice
    else:
        return int(n/slice)+1
