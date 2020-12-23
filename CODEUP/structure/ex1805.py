N = int(input())  # 사용자로부터 입력 기동장치의 개수 정수 N 입력
gas_device = []  # 입체기동장치 리스트
for i in range(N):  # N번 반복
    a, b = map(int, input().split())  # a: 식별번호, b: 가스 보유량 map함수를 이용
    gas_device.append([a, b])  # 입체기동자치 리스트에 리스트 형태로 저장[2차원 배열 사용]

gas_device.sort()  # 정렬 알고리즘 - 시간복잡도 nlogn -> gas_device[0]의 식별번호 오름차순 정렬이 됨
for i in range(N):  # 출력
    print(gas_device[i][0], gas_device[i][1])
