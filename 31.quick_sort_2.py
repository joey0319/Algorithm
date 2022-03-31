# 퀵정렬 일반적인 방식 / 시간이 좀 덜 걸림
def quickSort(lst, start, end):
    if start >= end: # 원소가 하나이면 종료
        return
    pivot = start # 피봇은 시작점
    left = start + 1 # 시작점 + 1부터 피봇보다 큰 수 탐색
    right = end # 끝점부터 피봇보다 작은 수 탐색
    while left <= right: # 교차되지 않을 때 까지 반복
        # 왼쪽 부터 보면서 피봇보다 큰 것 찾을때 까지 반복
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        # 끝 부터 보면서 피봇보다 작은 것 찾을때 까지 반복
        while right > start and lst[right] >= lst[pivot]:
            right -= 1
        if left > right: # 엇갈리면 피봇과 피봇보다 작은 데이터 교체
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            lst[left], lst[right] = lst[right], lst[left]
    
    # 최종적으로 엇갈려서 right 인덱스에 피봇이 위치해 있으므로
    # 피봇 기준으로 왼쪽 오른쪽에 대해 퀵정렬 재귀적 시행
    quickSort(lst, start, right - 1)
    quickSort(lst, right + 1, end)

lst = [1,-5,89,6,4,13,68]
quickSort(lst, 0, len(lst)-1)
print(lst)

# 퀵정렬 파이썬의 장점 활용한 방식 / 리턴을 받아와야 하므로 시간이 좀 더 걸림
def quick_sort(lst):
    # 리스트 원소가 하나거나 빈리스트이면 종료
    if len(lst) <= 1:
        return lst
    pivot = lst[0] # 피봇은 시작점
    tail = lst[1:] # tail은 피봇 제외 나머지

    # left는 tail중에 피봇보다 작거나 같은 값들
    left = [x for x in tail if x <= pivot]
    # right는 tail중에 피봇보다 큰 값들
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

array = [5,7,9,0,3,1,6,2,4,8]
print(quick_sort(array))



