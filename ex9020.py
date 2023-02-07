def solution(n):
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

answer = []
for _ in range(int(input())):
    num = int(input())

    a, b = num//2, num//2
    while a > 0:

        if solution(a) and solution(b):
            answer.append([a, b])
            break
        else:
            a -= 1
            b += 1
for ans in answer:
    print(' '.join(str(a) for a in ans))
