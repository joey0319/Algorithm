def partitionH(s, e): # 피봇을 시작점으로 본것
    p = s # 피봇이 s라는 뜻
    lp = s + 1
    rp = e
    while lp <= rp:
        while lp <= e and lst[p] >= lst[lp]: # 피봇보다 작은것을 찾는다. / 둘중에 하나에는 등호를 넣어 줘야한다.(피봇값과 같은 값이 있을경우 대비)
            lp += 1 # 증가하다가 인덱스 안넘도록 lp <= e
        while rp >= s and lst[p] < lst[rp]: # 피봇보다 큰것을 찾는다.
            rp -= 1 # 빼지다가 인덱스 안넘도록 s <= rp
        if lp < rp: # 무조건 교환하면 안되고 lp가 더작을때(좌측에 있을때)만
            lst[lp], lst[rp] = lst[rp], lst[lp]
    lst[rp], lst[p] = lst[p], lst[rp]
    return rp


def partitionL(s, e): # 피봇을 끝점으로 본것
    p = e
    i = s-1
    for j in range(s, e):
        if lst[p] > lst[j]:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[p], lst[i] = lst[i], lst[p]
    return i


# 퀵정렬 / 피봇이 좌측인 경우
def quickSort(s, e):
    if s < e: # 시작점(s)가 끝점(e)보다 작은 경우에만
        pivot = partitionL(s, e) 
        quickSort(s, pivot-1)
        quickSort(pivot+1, e)


lst = [12,69,10,30,2,16,8,31,22]
quickSort(0,len(lst)-1)
print(lst)