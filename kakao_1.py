m = 6 # i
n = 4 #j
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

def floodfill(val, i, j):
    # val은 같은 수일때만 sum을 늘리기 위해서다.
    picture[i][j] = 0
    # 한번 왔다간 곳에는 0으로 표시한다.
    sum = 1
    if j - 1 > 0 and picture[i][j-1] == val :
        picture[i][j-1] = 0
        sum += floodfill(val, i, j-1)

    if i - 1 > 0 and picture[i-1][j] == val :
        picture[i-1][j] = 0
        sum += floodfill(val, i-1, j)

    if i + 1 < m and picture[i+1][j] == val :
        picture[i+1][j] = 0
        sum += floodfill(val, i+1, j)

    if j + 1 < n and picture[i][j+1] == val :
        picture[i][j+1] = 0
        sum += floodfill(val, i, j+1)
    return sum


area = []

for i in range(m):
    for j in range(n):
        if picture[i][j] is 0 :
            continue
        area.append( floodfill(picture[i][j], i, j) )

answer = [0, 0]
answer[0] = len(area)
answer[1] = max(area)

print(answer)
