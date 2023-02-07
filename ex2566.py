answer = []
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
         answer.append([arr[j], i, j])
print(max(answer)[0])
print(max(answer)[1]+1, max(answer)[2]+1)