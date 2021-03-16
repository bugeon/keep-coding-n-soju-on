import heapq


def solution(scoville, K):

    scoville = sorted(scoville)

    heap = scoville

    lowest_scoville = heapq.heappop(heap)
    loop = 0
    while lowest_scoville < K:
        if not heap:
            return -1

        second_lowest_scoville = heapq.heappop(heap)
        if second_lowest_scoville == 0:
            return -1

        heapq.heappush(heap, second_lowest_scoville*2 + lowest_scoville)
        loop += 1
        lowest_scoville = heapq.heappop(heap)

    return loop


print(solution([1, 2, 3, 9, 10, 12]	, 7))