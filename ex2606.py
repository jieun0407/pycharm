n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)
answer = 1
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
answer = 0
def dfs(i):
    global answer
    visited[i] = 1
    for j in range(1, n+1):
        if visited[j] == 0 and graph[i][j] == 1:
            answer += 1
            dfs(j)


dfs(1)
print(answer)