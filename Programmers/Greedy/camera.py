def solution(routes):
	answer = 0
	cur_end = -35000
	
	for r in sorted(routes, key=lambda x: x[1]):
		if r[0] > cur_end:
			answer += 1
			cur_end = r[1]
	
	return answer
