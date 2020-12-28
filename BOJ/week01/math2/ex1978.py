def isPrime(N):
    if N == 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


N = int(input())
nums = list(map(int, input().split()))
count = 0
for i in nums:
    count += isPrime(i)
print(count)
