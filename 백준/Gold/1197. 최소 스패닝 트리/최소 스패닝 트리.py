import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

##############
# Union Find #
##############

    
def solution(graph):
    # UnionFind 초기화
    parent = list(range(v+1))
    for i in range(v+1):
        parent[i] = i

    def union(x, y):
        x = parent[x]
        y = parent[y]
        parent[y] = x
        
    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]

    # 1. 그래프 간선을 가중치 오름차순으로 정렬
    graph = sorted(graph, key=lambda x : x[2])

    # 2. 간선 연결
    total_edges = 0
    total_rank = 0
    for i in graph:
        if total_edges < v - 1:
            v1 = i[0]
            v2 = i[1]
            rank = i[2]

            # 사이클 탐지
            v1_parent = find(v1)
            v2_parent = find(v2)

            # 사이클 X
            if v1_parent != v2_parent:
                union(min(v1, v2), max(v1, v2))
                total_edges += 1
                total_rank += rank

    print(total_rank)

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(e)]
    solution(graph)