# 블랙잭 N개의 카드 중 3장을 골랐을 때 M을 넘지 않는 3장의 최대합을 출력하는 문제
# 파이썬 itertools 모듈을 이용한 풀이
from itertools import combinations  # 조합을 이용
# 카드의 개수 N (3 <= N <= 100), 카드의 합 M(10 <= M <= 300,000)
N, M = map(int, input().split())
card_list = list(map(int, input().split()))  # 카드 뭉치
sum_list = []

for i in list(combinations(card_list, 3)):  # N개의 카드 뭉치에서 3장의 조합을 모두 반본묵에 넣어줌
    if sum(i) <= M:  # 카드 3장의 총합이 M보다 작거나 같으면 리스트에 추가
        sum_list.append(sum(i))
print(max(sum_list))  # 가장 큰 값을 출력
