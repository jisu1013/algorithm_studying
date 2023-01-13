from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        d = q.popleft()
        for direc in directions:
            if 0 <= d[0]+direc[0] < h and 0 <= d[1]+direc[1] < w: 
                if visited[d[0]+direc[0]][d[1]+direc[1]] == 0 and mapp[d[0]+direc[0]][d[1]+direc[1]] == 1:
                    mapp[d[0]+direc[0]][d[1]+direc[1]] = 0
                    visited[d[0]+direc[0]][d[1]+direc[1]] = 1
                    q.append([d[0]+direc[0], d[1]+direc[1]])

while True:
    directions = [(1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1)]
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mapp = [[0]*w for i in range(h)]
    result = 0   
    for i in range(h):    
        nums = list(map(int, input().split()))
        for j in range(w):
            mapp[i][j] = nums[j]
    visited = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1:
                result += 1 
    print(result)
