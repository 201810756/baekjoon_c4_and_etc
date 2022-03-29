import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split()) # map : NxM 행렬
board=[]
INF=1e9
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def sol():
    queue=deque()
    v=[[[0]*2 for _ in range(M)]for _ in range(N)]
    v[0][0][0]=1 # 시작 칸 count
    queue.append((0,0,0))
    while queue:
        x,y,flag=queue.popleft()
        if x==(N-1) and y==(M-1):
            return v[N-1][M-1][flag]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and v[nx][ny][flag]==0: # 범위를 벗어나지 않고, 방문하지 않은 칸에 대해
                if board[nx][ny]==0: # 그냥 지나갈 수 있음
                    v[nx][ny][flag]=v[x][y][flag]+1
                    queue.append((nx,ny,flag))
                elif board[nx][ny]==1 and flag==0: # 벽이 있고, 아직 부순적이 없는 경우에는 ...
                    v[nx][ny][1]=v[x][y][flag]+1
                    queue.append((nx,ny,1))
    return -1 # 경로 실패
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
result=sol()
print(result)
"""
최단경로 => BFS 해결 
여기서 '벽을 부순다' 의 조건이 추가되었음
이 조건만 없으면 그냥 기본 BFS 문제 
처음처럼 그냥 무작정 브루트포스마냥 모든 경우의 수를 체크한다면 
N,M의 범위가 1,000까지이므로 시간초과 발생
따라서 벽을 부수는 행위에 대한 분기가 필요 (부순상태 vs 안부순상태)
이를 flag변수에 저장하여 
3차원 리스트로 정보 전달 << 여기서 3차원 리스트를 써야겠다는 생각을 하는것이 어려운 것 같다.
"""




"""
# 첫 시도(시간초과)
# 단순히 행렬 내 모든 요소를 돌면서 '1'에 해당하는 칸을 '0'으로 바꿔서 계산
# 그렇게 최단거리를 출력, 만약 경로가 없으면 INF 반환하여 -1 출력하는 방식으로 작성
# 하지만 시간초과 발생
# 시간초과 어째 해결 ? 
def sol(board):
    cnt=[[1]*M for _ in range(N)]
    v=[[False]*M for _ in range(N)]
    queue=deque()
    queue.append((0,0))
    v[0][0]=True
    while queue:
        x,y=queue.popleft()
        if x==(N-1) and y==(M-1):
            return cnt[N-1][M-1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and not v[nx][ny] and board[nx][ny]==0:
                cnt[nx][ny]=cnt[x][y]+1
                v[nx][ny]=True
                queue.append((nx,ny))
    return INF
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().rstrip())))
    # 0 : 이동가능, 1 : 이동불가
    # (0,0)->(N-1,M-1)
    # 최단 거리 출력, 불가능 시 출력 => -1
    # 시작,끝칸 포함
result=sol(board) # original board 
v=[[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]==1 and not v[i][j]:
            v[i][j]=True
            board[i][j]=0
            result=min(result,sol(board))
            board[i][j]=1
if result==INF:
    print(-1)
else:
    print(result)
"""