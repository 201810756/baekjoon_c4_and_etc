import sys
from collections import deque
T=int(sys.stdin.readline()) # 테스트 케이스
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]
def sol(start,target):
    queue=deque()
    v=[[False]*l for _ in range(l)]
    queue.append(start)
    tx,ty=target
    while queue:
        x,y=queue.popleft()
        if tx==x and ty==y:
            print(board[tx][ty])
            break
        v[x][y]=True
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and not v[nx][ny]:
                board[nx][ny]=board[x][y]+1
                v[nx][ny]=True
                queue.append((nx,ny))

for _ in range(T):
    l=int(sys.stdin.readline()) # l: 체스판 한변의 길이 (l x l)
    board=[[0]*l for _ in range(l)]
    a1,b1=map(int,sys.stdin.readline().split()) # (a1,b1) 현재 나이트
    a2,b2=map(int,sys.stdin.readline().split()) # (a2,b2) 나이트가 이동하려고 하는 칸
    # 나이트가 최소 몇 번만에 이동할 수 있는지 출력
    sol((a1,b1),(a2,b2))

