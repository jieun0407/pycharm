N = int(input())
M = int(input())
sosu = []

for num in range(N, M+1):
    error = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                error += 1
                break
        if error == 0:
            sosu.append(num)
if len(sosu) == 0:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
