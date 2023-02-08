N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(i):
    visited[i] = 1
    for j in range(1, N+1):
        if graph[i][j] == 1 and visited[j] == 0:
            dfs(j)
answer = 0
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        answer += 1

print(answer)

from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
        return maps[len(maps) - 1][len(maps[0]) - 1]

    answer = bfs(0, 0)
    return -1 if answer == 1 else answer