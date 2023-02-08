def dfs(begin, target, words, visited):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer

        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                if visited[i] != 0:
                    continue
                visited[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0 for n in words]

    answer = dfs(begin, target, words, visited)
    return answer


def solution(tickets):
    answer = [tickets[0][0]]
    visited = [0] * len(tickets)

    def dfs(x, y):
        visited[x] = 1
        answer.append(tickets[x][1])
        for i in range(len(tickets)):
            if visited[i] == 0 and tickets[i][0] == tickets[x][1]:
                dfs(i, 0)

    start = [tickets[i][0] for i in range(len(tickets))]
    finish = [tickets[i][1] for i in range(len(tickets))]
    if start.count("ICN") > 1:
        rev = sorted([[b, a] for a, b in tickets if a == 'ICN'])
        dfs(finish.index(rev[0][0]), 0)

    dfs(0, 0)
    return answer