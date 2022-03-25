import sys
# 1번 집부터 N번 집이 순서대로 있음
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠함
# 규칙 1 : 1번 집의 색은 2번 집의 색과 같지 않다
# 규칙 2 : N번 집의 색은 N-1번 집의 색과 같지 않다
# 규칙 3 : i번 집의 색은 i-1,i+1번 집의 색과 같지 않다.
# 이 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값
N=int(sys.stdin.readline())# 집의 수
houses=[]
for _ in range(N):
    R,G,B=map(int,sys.stdin.readline().split())
    houses.append([R,G,B])
for i in range(1,N):
    houses[i][0]+=min(houses[i-1][1],houses[i-1][2])
    houses[i][1]+=min(houses[i-1][0],houses[i-1][2])
    houses[i][2]+=min(houses[i-1][0],houses[i-1][1])
print(min(houses[N-1]))

"""
DP문제는 점화식을 구하면 쉽게 해결할 수 있음
이 문제에서도 조건만 잘 분석한다면 
현재 R,G,B 까지의 최소합은 자신의 색을 제외한 각 색의 합 중에 최소와의 합임을 알 수 있다.
즉 점화식 자체로만 생각하면 
(cur,Red)=(cur,Red)+min((prev,Blue),(prev,Green))
(cur,Green)=(cur,Green)+min((prev,Blue),(prev,Red))
(cur,Blue)=(cur,Blue)+min((prev,Blue),(prev,Red))
따라서 이 점화식을 그대로 옮겨주면 된다.
여기서 탐욕으로 풀 수 없는 이유는 가능한 색 중에 최소 값을 계속 더한다하더라도 
앞의 색으로 인해 선택 불가능한 색 조합이 더 최적의 결과를 가져올 수 있기 때문
"""