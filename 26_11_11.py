#제곱수 판별하기
def solution(n):
    for a in range(n):
        if n==a*a:
            return 1
    return 2   
