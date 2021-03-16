from collections import deque

def solution(progresses, speeds):
	answer = []
	progresses = deque(progresses)
	speeds = deque(speeds)

	while progresses:
		finished = 0
		while progresses and progresses[0] >= 100:
			progresses.popleft()
			speeds.popleft()
			finished += 1
		if finished != 0:
			answer.append(finished)
		for i in range(len(progresses)):
			progresses[i] += speeds[i]

	return answer

progresses, speeds = [93, 30, 55], [1, 30, 5]
print(solution(progresses, speeds)) #	[2, 1]
progresses, speeds = [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds)) #	[1, 3, 2]