n = int(input())  # 사용자로부터 입력받을 피보나치 인덱스


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


print(fibo(n))
