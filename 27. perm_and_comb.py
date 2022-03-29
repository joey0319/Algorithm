# 순열 생성하는 함수
def perm(n, depth, P):
    result = []
    if depth == n:
        return [P]
    else:
        for i in range(len(arr)):
            if choosen[i] == True:
                continue
            choosen[i] = True
            result += perm(n, depth+1, P+[i])
            choosen[i] = False
    return result

arr = [1,2,3,4,5]
choosen = [False for _ in range(len(arr))]
print(perm(2,0,[]))

# 조합을 만드는 함수
def comb(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in comb(rest_arr, n-1):
            result.append([elem] + c)
    return result

print(comb(arr, 2))