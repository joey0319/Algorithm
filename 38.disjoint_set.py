# 서로소 집합을 만드는 함수

#1. 집합들을 저장할 배열과 랭크를 저장할 배열을 만들어준다. (1부터 10까지 수라고 가정)


N = 10
# 0인덱스는 버리고 group의 의미는 자기 자신의 인덱스가 부모를 나타낸다.
# 인덱스와 부모가 같다면 그 번호는 집합이 자기혼자만 구성되어 있는것
group = list(range(N+1))
rank = [0] * (N+1)

#2. x의 최종 대표를 찾는 findset 함수
def find_set(x):
    # 인덱스와 키값이 같지 않다면 대표가 자기 자신이 아니므로
    # 재귀적으로 올라가 최종 대표를 찾고 그 값을 키값으로 넣어준다.
    if x != group[x]:
        group[x] = find_set(x)
    return group[x]

#3. 두수를 합집합 시키는 union 함수와 그에 필요한 link 함수

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    # y의 랭크가 크면 y를 대표로 지정
    if rank[x] < rank[y]:
        group[x] = y
    else:
        # x의 랭크가 y보다 크거나 같은 경우 x를 대표로 지정
        group[y] = x
        # 만약에 같으면 x의 랭크 1추가(왜냐하면 x를 대표로 지정했기 때문)
        if rank[x] == rank[y]:
            rank[x] += 1

