import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K:
        lowest = heapq.heappop(scoville)
        second_lowest = heapq.heappop(scoville)
        new_scoville = lowest + (second_lowest * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return answer
