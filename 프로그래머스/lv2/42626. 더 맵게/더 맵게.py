import heapq

def solution(scoville, k):
    # 힙은 push(), pop() 이후 자동 정렬
    heap = []
    # 모든 원소를 차례대로 힙에 삽입
    for i in scoville:
        heapq.heappush(heap, i)

    cnt = 0
    # 모든 스코빌이(최솟값) k이상일 때까지
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        cnt += 1
    return cnt