from sys import stdin
N = int(input())

graph = [[0]*(N) for _ in range(N)]
visited = [[0]*(N) for _ in range(N)]

for i in range(N):
    #M = map(int, input())
    M = stdin.readline().strip()
    for j, value in enumerate(M):
        graph[i][j] = int(value)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
    visited[x][y] = 1
    global nums
    if graph[x][y] == 1:
        nums += 1
    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N:
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dfs(nx, ny, c)


cnt = 1 # 아파트 단지를 세기 위한
numlist = [] # 아파트 단지별 숫자
nums = 0 # 아파트 수
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b, cnt)
            numlist.append(nums)
            nums = 0
print(len(numlist))
for n in sorted(numlist):
    print(n)