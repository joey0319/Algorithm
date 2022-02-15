# 9 X 9 스도쿠에서 3 X 3 섹션으로 나눌 때

sudoku = [[1,2,3,4,5,6,7,8,9] for _ in range(9)]

section_list = []
for i in range(0,9,3):
    for j in range(0,9,3): # 시작점 좌측상단을 기준으로
        section = []
        for k in range(i, i+3):
            for l in range(j, j+3):
                section.append(sudoku[k][l])
        section_list.append(section) 

print(sudoku)
print(section_list)