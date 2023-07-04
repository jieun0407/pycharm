N, M = map(int, input().split())
origin = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = origin[i-1:j]
    temp.reverse()
    origin[i-1:j] = temp

for i in range(N):
    print(origin[i], end=' ')