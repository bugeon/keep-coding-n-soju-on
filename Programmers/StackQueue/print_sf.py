from collections import deque


def solution(priorities, location):
	answer = 0
	wait_list = deque()
	for p in priorities:
		wait_list.append(p)
	target_location = location

	while True:
		current = wait_list.popleft()
		if len(wait_list) == 0 or current >= max(wait_list):
			answer += 1
			if target_location == 0:
				break
			else:
				target_location -= 1
		else:
			wait_list.append(current)
			if target_location == 0:
				target_location = len(wait_list) - 1
			else:
				target_location -= 1
	return answer

'''
best answer

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''
