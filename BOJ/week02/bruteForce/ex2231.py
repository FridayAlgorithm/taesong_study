N = int(input())  # 정수 N 입력 받음
for i in range(1, N+1):  # N보다 작은 수까지 완전 탐색을 진행
    num = str(i)  # 자리수의 합을 위해서 문자열로 변환한 값을 num에 저장
    count = i  # 생성수를 만들기 위해서 count 변수에 i를 대입
    for j in range(len(num)):  # num의 자리수만큼 반복
        count += int(num[j])  # 일의 자리수부터 덧셈
    if count == N:  # 생성수의 값이 N값과 동일하다면
        print(i)  # N의 생성수 i를 출력
        break  # 반복문을 종료
if i == N:  # 반복문을 다 돌았는데 없으면 해당 수는 생성수가 존재하지 않음
    print(0)  # 0 출력
