import heapq

def solution(S, K):
    heap = S
    heapq.heapify(heap)

    cnt = 0
    while heap[0] < K and len(heap) >= 2:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a + (b * 2))
        cnt += 1
    else:
        if heapq.heappop(heap) < K:
            return -1

    return cnt