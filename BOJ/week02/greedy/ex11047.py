N, K = map(int, input().split())
coin_list = []
for i in range(N):
    coin = int(input())
    coin_list.append(coin)

coin_list.reverse()
count = 0
for j in coin_list:
    count += K // j
    K %= j
print(count)
