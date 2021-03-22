def solution(ciatations):
	answer = 0
	ciatations = sorted(ciatations, reverse=True)
	
	for i in range(1, len(ciatations)):
		if ciatations[i-1] >= i:
			if ciatations[i] <= i:
				answer = i
			elif i == (len(ciatations) - 1):
				answer = i+1
	if len(ciatations) == 1:
		answer = 1
	return answer
