def solution(numbers):
	answer = str()
	for n in sorted([(n, (str(n)*4)[:4]) for n in numbers], key=lambda x: x[1], reverse=True):
		if not (answer == '' and n[0] == 0):
			answer += str(n[0])
	if answer == '':
		answer = '0'
	return answer
