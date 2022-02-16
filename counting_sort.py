# 리스트 안에 각 항목이 몇개 있는지 세는 작업 / .count() 메서드와 동일
# 숫자의 범위와 리스트가 주어진다.(범위 중 제일 큰 정수 N만 알면된다.)

def counting_sort(lst, N):
    counts = [0]*(N+1)
    for number in range(N+1):
        for idx in range(len(lst)):
            if lst[idx] == number:
                counts[number] += 1  # 여기까지 하면 counts라는 리스트에는 각 숫자(=인덱스)의 발생횟수가 들어가 있다.

    for i in range(len(counts)-1):
        counts[i+1] += counts[i]  # 이 작업은 i 라는 숫자 앞에 몇개의 숫자가 있는지 세는 것
    
    temp = [0]*len(lst)
    for j in range(len(lst)-1, -1, -1):
        counts[lst[j]] -= 1
        temp[counts[lst[j]]] = lst[j]

    return temp




