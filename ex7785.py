import sys
input = sys.stdin.readline

n = int(input())
_dict = {}
for _ in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        _dict[name] = status
    else:
        del _dict[name]
_dict = sorted(_dict.keys(), reverse=True)

for i in _dict:
    print(i)
