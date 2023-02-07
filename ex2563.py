N = int(input())
black = []
for i in range(N):
    sqr = list(map(int, input().split()))
    black.append(sqr)
print(max(a[0] for a in black))
print(max(a[1] for a in black))