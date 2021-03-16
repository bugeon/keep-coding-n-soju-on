from collections import deque

def solution(priorities, location):
	answer = 0

	dq = deque((priority, i) for i, priority in enumerate(priorities))

	while dq:
		current = dq.popleft()

		if dq and current[0] < max(dq)[0]:
			dq.append(current)
			continue
		answer += 1
		if current[1] == location:
			return answer


priorities, location = [2, 1, 3, 2], 2
print(solution(priorities, location)) # 1
priorities, location = [1, 1, 9, 1, 1, 1], 0
print(solution(priorities, location)) # 5