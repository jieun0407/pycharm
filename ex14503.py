import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

vaccum_move_map = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())

vaccum_move_map[x][y] = 1

vaccum_map = []
for i in range(n):
    vaccum_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

