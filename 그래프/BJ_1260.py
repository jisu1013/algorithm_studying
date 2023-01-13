# DFS는 stack # BFS는 queue 
from collections import deque

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False]*(n+1)
bfs_visited = [False]*(n+1)
for i in range(m):
  start,end = map(int, input().split())
  graph[start].append(end)
  graph[end].append(start)
for i in range(1, n+1):
  graph[i].sort()

#우선 DFS 경우, stack
def dfs(v):
  print(v, end=' ')
  dfs_visited[v] = True
  for i in graph[v]:
    if not dfs_visited[i]:
      dfs(i)
# BFS , deque 사용
def bfs(start):
  q = deque()
  q.append(start)
  bfs_visited[start] = True
  while q:
    next_ = q.popleft()  
    print(next_, end=' ')
    for i in graph[next_]:
      if not bfs_visited[i]:
        q.append(i)
        bfs_visited[i] = True
dfs(v)
print()
bfs(v)
print()
