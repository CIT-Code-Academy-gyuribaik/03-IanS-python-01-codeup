

#피자 나눠 먹기 (3)
def solution(slice, n):
    if n%slice==0:
        return n/slice
    else:
        return int(n/slice)+1
