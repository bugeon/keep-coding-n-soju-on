def solution(participant, completion):
	num = 0
	parti = dict()
	for p in participant:
		h = hash(p)
		parti[h] = p
		num += h
	for c in completion:
		num -= hash(c)

	answer = parti[num]

	return answer
