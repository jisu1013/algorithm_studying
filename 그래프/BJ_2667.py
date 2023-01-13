N = int(input())
graph = [[0]*N for _ in range(N)]
total = 0
houses = []
for i in range(N):
  line = input()
  for j in range(N):
    if int(line[j]) == 1:
      graph[i][j] = 1
visited = [[False]*N for _ in range(N)]
directions = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(i,j):
  global cnt
  visited[i][j] = True
  for move_i, move_j in directions:
    if 0 <=(i+move_i)< N and 0<=(j+move_j)< N:
      if not visited[i+move_i][j+move_j] and graph[i+move_i][j+move_j] == 1:
        #visited[i+move_i][j+move_j] = True
        dfs(i+move_i, j+move_j)
        cnt += 1

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1 and visited[i][j] == 0:
      global cnt
      cnt = 0
      dfs(i,j)
      total += 1
      houses.append(cnt+1)
print(total)
houses.sort()
for house in houses:
  print(house)
