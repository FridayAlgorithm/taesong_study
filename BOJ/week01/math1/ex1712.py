import sys

A, B, C = map(int, sys.stdin.readline().split())
# A : 고정, B: 가변, C: 노트북 가격

if B < C:
    print(int(A / (C - B)+1))
else:
    print(-1)
