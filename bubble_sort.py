# 인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식

# 1. 오름차순
def BubbleSort(lst):
    for practice in range(len(lst)-1):  # 리스트 길이-1 만큼만 시행하면 된다. 마지막은 할 필요가 없다.
        for idx in range(len(lst)-1):   # 리스트 길이-1 만큼만 해줘야 마지막 인덱스가 벗어나지 않는다.
            if lst[idx] > lst[idx+1]:
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]  # 한번 시행하면 제일 큰 수가 오른쪽으로 가있다.
    return lst
print(BubbleSort([56,78,1,9,101,37,113]))

# 2. 내림차순 / 오름차순에서 부등호만 바꿔준다.
def BubbleSort_reverse(lst):
    for practice in range(len(lst)-1):  
        for idx in range(len(lst)-1):   
            if lst[idx] < lst[idx+1]:  
                lst[idx], lst[idx+1] = lst[idx+1], lst[idx]  # 이렇게 한번 하면 제일 작은 수가 오른쪽으로 가게된다.
    return lst
print(BubbleSort_reverse([1,5,19,4,148,3,287]))


