import heapq


def solution(scoville, K):
	heapq.heapify(scoville)
	answer = 0
	
	while scoville[0] < K:
		s0 = heapq.heappop(scoville)
		answer += 1
		if len(scoville) > 0:
			s1 = heapq.heappop(scoville)
			heapq.heappush(scoville, s0 + (s1 * 2))
		else:
			answer = -1
			break
		
	return answer
