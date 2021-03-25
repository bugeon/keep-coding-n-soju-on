def solution(brown, yellow):
	answer = list()
	for i in range(3, brown-2):
		find = False
		for j in range(3, brown-2):
			if i < j:
				break
			if ((2 * i) + (2 * j)) - 4 == brown and (i-2)*(j-2) == yellow:
				answer = [i, j]
				find = True
				break
		if find:
			break
	
	return answer
