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
#배열의 평균값
def solution(numbers):
    return sum(numbers)/len(numbers)
#아이스 아메리카노
def solution(money):
    return [money//5500,money%5500]
#배열 뒤집기
def solution(num_list):
    num_list.reverse()  
    return num_list
