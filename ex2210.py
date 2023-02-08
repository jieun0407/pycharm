def dfs(x, y, num):
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if 0<=ddx<5 and 0<=ddy<5:
            dfs(ddx, ddy, num+graph[ddx][ddy])

graph = [list(map(str, input().split())) for _ in range(5)]

result = []

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(result))

"""
def dfs(x, y, num):
    if len(num) == 6:  # 6자리 숫자가 만들어졌다면
        if num not in result:  # result에 없다면
            result.append(num)
        return

    dx = [1, -1, 0, 0]  # 상하좌우 확인 x
    dy = [0, 0, 1, -1]  # 상하좌우 확인 y
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]

        if 0 <= ddx < 5 and 0 <= ddy < 5:  # 범위 내에 있다면
            dfs(ddx, ddy, num + graph[ddx][ddy])  # 6글자가 될 때 까지 재귀


# 입력
graph = [list(map(str, input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])  # 0,0부터 4,4까지 모두 검사
print(len(result))
"""