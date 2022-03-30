# 병합정렬(오름차순) / 이것은 기본 개념이고 인덱스로 위치교환하는게 효율적이다.
def merge(left, right):
    result = []
    lp = rp = 0  # left = [8,10,30,69] / right = [8,16,22,31]일때
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            result.append(left[lp]) # left가 작으면 left를 넣어준다.
            lp += 1
        else:
            result.append(right[rp]) # right가 작으면 right를 넣어준다.
            rp += 1
    # if lp < len(left):  # 왼쪽에 데이터가 남아있으면 왼쪽 데이터 전부 넣는다.
    while lp < len(left):
        result.append(left[lp])
        lp += 1
    # if rp < len(right): # 오른쪽 데이터 남아 있으면 오른쪽 데이터 전부넣는다.
    while rp < len(right):
        result.append(right[rp])
        rp += 1

    return result


def mergeSort(lst):
    # 재귀의 탈출 조건
    if len(lst) <= 1:  # 홀수 짝수에 의해 빈리스트가 보내지는 경우가 있으므로 부등호로
        return lst

    #중간지점을 계산
    m = len(lst) // 2
    # 중간기준 왼쪽 오른쪽을 다시 병합정렬(재귀)
    left = mergeSort(lst[:m])
    right = mergeSort(lst[m:])
    result = merge(left, right)

    return result

lst = [69,10,30,2,16,8,31,22]
print(mergeSort(lst))