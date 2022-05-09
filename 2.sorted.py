# 1. 리스트를 정렬하는 sorted함수
# 문자는 a,b,c 순이 오름차순 / 숫자는 1,2,3 순이 오름차순

list = [45,22,6,8,56,100,1,9,201]
print('정렬전:', list)

sorted_list = sorted(list)
print('오름차순 정렬:', sorted_list)

reverse_list = sorted(list, reverse = True)
print('내림차순 정렬:', reverse_list)

#1-2. 2차원리스트를 인덱스 2를 기준으로 정렬하는 방법
lst = [
    [1,2,3],
    [0,4,2],
    [10,23,1],
    [1,6,16]
]
sorted_lst = sorted(lst, key=lambda lst: lst[2])
print('2차원리스트 인덱스 2기준 정렬:', sorted_lst)

# 2. vlaue를 기준으로 딕셔너리 정렬하는 sorted 함수

foods = {'햄버거':90, '참치':150, '소고기':170, '회':5}
print('정렬전', foods)

sort_dict = sorted(foods.items(), key=lambda x:x[1])
print('오름차순 정렬:', sort_dict)

reverse_dict = sorted(foods.items(), key=(lambda x:x[1]), reverse = True)
print('내림차순 정렬:', reverse_dict)

# 3. key를 기준으로 딕셔너리 정렬하는 sorted 함수 / 결과는 키가 정렬된 리스트

foods = {'햄버거':90, '참치':150, '소고기':170, '회':5}
print('정렬전', foods)

sort_dict = sorted(foods)
print('오름차순 정렬:', sort_dict)

reverse_dict = sorted(foods, reverse = True)
print('내림차순 정렬:', reverse_dict)

# 4. 리스트안의 딕셔너리 여러개가 있을 때 딕셔너리 정렬하는 sorted 함수

dict_list = [{'coin':'btc', 'price':5000},{'coin':'eth', 'price':200},{'coin':'rvn', 'price':500}]
print('정렬전:', dict_list)

sorted_coin_list = sorted(dict_list, key=(lambda x: x['coin'])) #coin의 value를 기준으로 정렬
print('key=coin으로 오름차순:', sorted_coin_list)

reverse_coin_list = sorted(dict_list, key=(lambda x: x['coin']), reverse = True)
print('key=coin으로 내림차순:', reverse_coin_list)

sorted_price_list = sorted(dict_list, key=(lambda x: x['price']))
print('key=price로 오름차순', sorted_price_list)

reverse_price_list = sorted(dict_list, key=(lambda x: x['price']), reverse = True)
print('key=price로 내림차순', reverse_price_list)


