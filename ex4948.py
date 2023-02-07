"""
answer = True
array = []
while answer:
    n = int(input())
    sosu = 0

    if n== 0:
        break
    for num in range(n+1, 2*n+1):
        error = 0
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                error += 1
        if error == 0:
            sosu += 1
    array.append(sosu)

for j in array:
    print(j)
"""
def sosu(x):
    if x==1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
list = list(range(2, 246912))
memo = []
for i in list:
    if sosu(i):
        memo.append(i)
n = int(input())
while True:
    count = 0
    if n == 0:
        break
    for i in memo:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())
