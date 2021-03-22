import heapq


def solution(operations):
	answer = []
	answer_list = list()
	for o in operations:
		s = o.split(' ')
		if s[0] == 'I':
			heapq.heappush(answer_list, int(s[1]))
		elif s[0] == 'D' and s[1] == '-1' and len(answer_list):
			heapq.heappop(answer_list)
		elif s[0] == 'D' and s[1] == '1' and len(answer_list):
			answer_list = heapq.nlargest(len(answer_list), answer_list)
			heapq.heappop(answer_list)
			heapq.heapify(answer_list)

	if len(answer_list) == 0:
		answer = [0, 0]
	elif len(answer_list) == 1:
		min = heapq.heappop(answer_list)
		answer = [min, min]
	else:
		answer_list = heapq.nlargest(len(answer_list), answer_list)
		max = heapq.heappop(answer_list)
		heapq.heapify(answer_list)
		min = heapq.heappop(answer_list)
		answer = [max, min]
	return answer
