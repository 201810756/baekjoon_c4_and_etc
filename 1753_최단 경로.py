import sys
import heapq
INF=1e9
V,E=map(int,sys.stdin.readline().split()) # V : 정점의 개수, E : 간선의 개수
info=[[] for _ in range(V+1)]
start=int(sys.stdin.readline())
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    info[u].append((v,w))
    # 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음


def sol(start):
    results=[INF]*(V+1)
    heap=[]
    heapq.heappush(heap,(0,start))
    results[start]=0
    while heap:
        dist,node=heapq.heappop(heap)
        if dist>results[node]:
            continue
        for finish,fee in info[node]:
            if results[finish]>dist+fee:
                results[finish]=dist+fee
                heapq.heappush(heap,(dist+fee,finish))
    for i in range(1,V+1):
        if results[i]==INF:
            print("INF")
        else:
            print(results[i])

sol(start)