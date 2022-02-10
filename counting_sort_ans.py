# counting_sort를 좀더 간단히 나타내보자

def Counting_Sort(lst, k): # A : 입력 리스트(0 to k) / C : 카운트 리스트
    
    C = [0]*(k+1)

    for i in range(len(lst)):
        C[lst[i]] += 1    # 이것은 counts 리스트를 만들어주는 것 / counts 리스트는 각 숫자의 개수를 담고있다.
        
    for i in range(1, len(C)):
        C[i] += C[i-1]   # 이것은 앞에 본인 몇개의 숫자가 있는지 count 리스트를 재정의 

    temp = [0] * (len(lst))
    for i in range(len(temp)-1,-1,-1):
        C[lst[i]] -= 1
        temp[C[lst[i]]] = lst[i] # 이것은 정렬된 리스트 temp를 만드는 과정

    return temp

print(Counting_Sort([0,2,1,1,3,4,3,5,4,4],5))
