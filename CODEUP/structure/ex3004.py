# 시간 초과 풀이 - why? index함수의 시간복잡도가 o(N)이므로 결과론적으로 o(N^2)
# N = int(input())
# nums = list(map(int, input().split()))
# sort_nums = sorted(nums)
# sort_index = []
# for i in nums:
#     a = sort_nums.index(i)
#     print(a, end=' ')


N = int(input())  # 사용자로부터 정수 N을 입력 받음
nums = list(map(int, input().split()))  # 입력 받은 수를 nums에 저장
sorted_nums = sorted(nums)  # 정렬 알고리즘 - O(nlogn)의 시간 복잡도

# 위의 시간 초과를 해결 하기 위해서 이진 탐색 알고리즘을 적용
# 시간 복잡도 O(logn)


def binary_search(data, start, end, k):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == k:
            return mid
        elif data[mid] < k:
            start = mid + 1
        else:
            end = mid - 1


# 시간 복잡도 O(logn) -> 원소가 n개니까 O(nlogn)
for i in range(N):
    print(binary_search(sorted_nums, 0, N-1, nums[i]), end=' ')
