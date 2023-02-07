"""
N, M = map(int, input().split())
A, B = [], []

for i in range(N):
    arr = list(map(int, input().split()))
    A.append(arr)
for i in range(N):
    arr = list(map(int, input().split()))
    B.append(arr)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()
"""
n,m,*a=map(int,open(0).read().split())
print(n,m,a)
for x in range(n):q=x*m;print(*map(sum,zip(a[q:q+m],a[q+n*m:q+n*m+m])))