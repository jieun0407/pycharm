A, B, C = map(int, input().split())
item = 0
bep = C * item - (A + B * item)
#C * item > (A + B * item)
#(C-B) item > A
if C-B < 0 and A > 0:
    print(-1)
while bep <=0:
    bep = C * item - (A + B * item)
    item += 1
print(item)
