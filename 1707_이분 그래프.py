# 이분 그래프
import sys
from collections import deque
# 그래프 내에 순회가 있으면 NO 아니면 YES ?
K=int(sys.stdin.readline()) # 테스트 케이스
def sol(node):
    queue=deque()
    queue.append(node)
    visited[node]=1
    while queue:
        node=queue.popleft()
        for l_node in board[node]:
            if visited[l_node] == 0:
                visited[l_node]=visited[node]*(-1)
                queue.append(l_node)
            else:
                if visited[l_node]==visited[node]: # 인접노드끼리 같으면
                    return False # 이분 그래프가 될 수 없음
    return True
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())  # V : 정점, E : 간선
    flag = 0
    board = [[] for _ in range(V+1)]
    visited=[0] * (V+1)
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())  # 인접한 두 정점 번호 u,v (u!=v)
        # 이분그래프면(Bipartite Graph) YES , 아니면 NO 출력
        board[u - 1].append(v - 1)
        board[v - 1].append(u - 1)
    for node in range(1,V+1):
        if visited[node]==0:
            if not sol(node):
                flag=1
                break
    if flag==1:
        print("NO")
    else:
        print("YES")
"""
인접한 노드가 같은 값을 가지면(색이라고들 함)
이분 그래프가 될 수 없음
bfs로 돌면서 윗 노드의 값에 -1을 해줌으로써 하위 노드로 이동함
그러다가 두 노드 모두 방문한 노드인데 같은 값을 가진다? 이분 그래프 조건 만족 x 
"""
"""틀림
def sol(board,start):
    queue=deque()
    visited = [False] * V
    check = [False] * V
    queue.append(start)
    while queue:
        start=queue.popleft()
        visited[start]=True
        for node in board[start]:
            if not visited[node]:
                visited[node]=True
                queue.append(node)
            elif visited[node]:
                if not check[node]:
                    check[node]=True
                elif check[node]:
                    return False
    return True

for _ in range(K):
    V,E=map(int,sys.stdin.readline().split()) # V : 정점, E : 간선
    flag=0
    board=[[]for _ in range(V)]
    for _ in range(E):
        u,v=map(int,sys.stdin.readline().split()) # 인접한 두 정점 번호 u,v (u!=v)
        # 이분그래프면(Bipartite Graph) YES , 아니면 NO 출력
        board[u-1].append(v-1)
        board[v-1].append(u-1)
    for node in range(V):
        if not sol(board,node):
            flag=1
            break
    if flag==1:
        print("NO")
    else:
        print("YES")"""



"""sol1(시간초과)
K=int(sys.stdin.readline()) # 테스트 케이스
def check(node,sets):
    flag=0
    for n in sets:
        if node in board[n]:
            flag=1
            return flag
    return flag
for _ in range(K):
    result_flag=0
    set_a=set()
    set_b=set()
    V,E=map(int,sys.stdin.readline().split()) # V : 정점, E : 간선
    board=[[]for _ in range(V)]
    for _ in range(E):
        u,v=map(int,sys.stdin.readline().split()) # 인접한 두 정점 번호 u,v (u!=v)
        # 이분그래프면(Bipartite Graph) YES , 아니면 NO 출력
        board[u-1].append(v-1)
        board[v-1].append(u-1)
    for i in range(V):
        flag=0
        if len(set_a)==0:
            set_a.add(i)
        else:
            if check(i,set_a)==0:
                set_a.add(i)
            elif check(i,set_b)==0:
                set_b.add(i)
            else:
                result_flag=1
                break
    if result_flag==1:
        print("NO")
    else:
        print("YES")"""

