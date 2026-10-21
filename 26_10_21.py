#양꼬치
def solution(n, k):
    f=n//10
    return 12000*n + 2000*(k-f)

#짝수의 합
def solution(n):
    sum=0
    while n%2==0:
        sum=sum+n
        n=n-2
        if n==0:
            break
    while n%2==1:
        n=n-1
        sum=sum+n
        n=n-2
        if n==0:
            break    
    return sum       

#배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
