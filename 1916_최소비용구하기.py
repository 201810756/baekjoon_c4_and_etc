"""
시간초과로 상당히 애 먹은 문제다
모든 경로를 확인한다면 시간초과가 발생한다.
결국 구글링과 백준 질문검색을 통해 해답을 발견했는데
sol함수 안에 우큐에서 팝 연산 후
거리 비교를 통해서 만약 results 저장 값보다 거리가 크다면 넘어가는 코드를
추가해주었더니 시간초과가 해결되었다.

출발&도착 노드가 정해져있으므로 다익스트라
"""
import sys
import heapq
INF=1e9 # 무한
N=int(sys.stdin.readline()) # 도시의 수
M=int(sys.stdin.readline()) # 버스의 수
info=[[] for _ in range(N+1)]
for _ in range(M):
    x,y,z=map(int,sys.stdin.readline().split())
    # x:출발도시, y:도착도시, z:비용
    info[x].append((y,z))
start,target=map(int,sys.stdin.readline().split()) # 출발지와 목적지

def sol(start,target):
    heap=[]
    heapq.heappush(heap,(0,start))
    results=[INF]*(N+1)
    results[start]=0
    while heap:
        dist,node=heapq.heappop(heap)
        if dist>results[node]:
            continue
        for finish,fee in info[node]:
            if results[finish]>dist+fee:
                results[finish]=dist+fee
                heapq.heappush(heap,(dist+fee,finish))
    print(results[target])

sol(start,target)