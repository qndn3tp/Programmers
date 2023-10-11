import sys, heapq

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

min_heap = []
max_heap = []
for n in nums:
    heapq.heappush(min_heap, n)
    heapq.heappush(max_heap, -n)

min = heapq.heappop(min_heap)
max = heapq.heappop(max_heap) * (-1)

print(min, max)