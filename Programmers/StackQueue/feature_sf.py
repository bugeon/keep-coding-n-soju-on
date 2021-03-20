import math


def solution(progresses, speeds):
	answer = list()
	remain = list()

	for i in range(len(progresses)):
		remain.append(math.ceil((100-progresses[i])/speeds[i]))
	deploy = 0
	deploy_base = remain[0]
	for i in range(len(remain)):
		deploy += 1
		if i == len(remain) - 1:
			answer.append(deploy)
			break
		if deploy_base < remain[i+1]:
			answer.append(deploy)
			deploy = 0
			deploy_base = remain[i+1]

	return answer
