from collections import deque


def solution(bridge_length, weight, truck_weights):
	answer = 0
	current_truck = 0
	truck_number = len(truck_weights)
	doing = deque()
	doing_weight = 0
	done = False

	while not done:
		pop_number = 0
		answer += 1
		for d in doing:
			d['position'] += 1
			if d['position'] > bridge_length:
				pop_number += 1
		for i in range(pop_number):
			doing_weight -= doing.popleft()['weight']

		if current_truck < truck_number and doing_weight + truck_weights[current_truck] <= weight:
			doing.append({'weight': truck_weights[current_truck], 'position': 1})
			doing_weight += truck_weights[current_truck]
			current_truck += 1

		if current_truck >= truck_number and len(doing) < 1:
			done = True

	return answer

```
정확성  테스트
테스트 1 〉	통과 (2.83ms, 10.2MB)
테스트 2 〉	통과 (17.96ms, 10.2MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (62.49ms, 10.2MB)
테스트 5 〉	통과 (411.02ms, 10.1MB)
테스트 6 〉	통과 (171.97ms, 10.3MB)
테스트 7 〉	통과 (1.29ms, 10.2MB)
테스트 8 〉	통과 (0.34ms, 10.3MB)
테스트 9 〉	통과 (5.35ms, 10.3MB)
테스트 10 〉	통과 (0.32ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.49ms, 10.2MB)
테스트 13 〉	통과 (1.79ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```
