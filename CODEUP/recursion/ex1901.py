n = int(input())  # 정수 n을 입력 받음


def integer_print(a):  # 재귀 함수
    if a == 0:  # 종료 조건
        return
    else:
        print(n-a+1)  # 순서대로 출력
        integer_print(a-1)  # 자기 자신 호출


integer_print(n)  # 함수 호출
