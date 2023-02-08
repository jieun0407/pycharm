n, m, v = map(int, input().split())
# 인접 영행렬 생성
graph = [[0] * (n+1) for _ in range(n+1)]
# 방문한 곳 체크를 위한 배열 선언
visited = [0] * (n+1)

# 입력 받는 두 값에 대해 영행렬에 1 삽입
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    #방문한 곳은 1 넣기
    visited[v] = 1
    print(v, end=' ')
    # 재귀 함수 선언(v와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)
from collections import deque
def bfs(v):
    # 방문해야 할 곳을 순서대로 넣을 큐
    queue = deque([v])
    # dfs를 완료한 visited 배열(1로 되어있음)에서 0으로 방문 체크
    visited[v] = 0
    # 큐 안에 데이터 없을 때 까지
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0



dfs(v)
print()
bfs(v)