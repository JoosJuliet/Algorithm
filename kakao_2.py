m = 3# i
n = 6 #j
city_map = [[0, 2, 0, 0, 0, 2], [0, 0, 2, 0, 1, 0], [1, 0, 0, 2, 2, 0]]
route = [[0] * (n) for _ in range(m)]

for j in range(n):
    if city_map[0][j] == 0 or city_map[0][j] == 2:
        route[0][j] = 1
    if city_map[0][j] == 1 :
        for k in range(j,n):
            route[0][k] = 0
        break

for i in range(m):
    if city_map[i][0] == 0 or city_map[i][0] == 2 :
        route[i][0] = 1
    if city_map[i][0] == 1 :
        for k in range(i,m):
            route[k][0] = 0
        break

# 이건 


def judgment_route(i, j):
    if city_map[i][j] == 0 :
        if j-1 < n and i-1 < m and route[i][j] is 0 :
            route[i][j] += (route[i][j-1] + route[i-1][j])

    if city_map[i][j] == 1 :
        if j-1< n and i -1 < m and route[i][j] is 0 :
            route[i][j] = 0

    if city_map[i][j] == 2 :
        if j-1 < n and i-1 < m and route[i][j] is 0 :
            # route[i][j] += (route[i][j-1] + route[i-1][j])
            # 없어도 된다. 어차피 이건 뭐가 있든 의미가 없으니까
            if i+1 < m :
                route[i+1][j] = route[i-1][j]
            if j+1 < n :
                route[i][j+1] = route[i][j-1]


route[0][0] = 1

for k in range(m):
    for l in range(n):
        judgment_route(k, l)
print(route)
