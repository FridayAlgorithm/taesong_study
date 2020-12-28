def isPrime(N):
    if N == 1:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True


M = int(input())
N = int(input())
isPrime_list = []
count = 0

for i in range(M, N+1):
    if isPrime(i):
        isPrime_list.append(i)
if isPrime_list:
    print(sum(isPrime_list))
    print(isPrime_list[0])
else:
    print(-1)
