def solution(bridge_length, weight, truck_weights):
	total_time = 0
	bridge = [0] * bridge_length

	while bridge:
		total_time += 1
		bridge.pop(0)

		if truck_weights:
			if sum(bridge) + truck_weights[0] <= weight:
				bridge.append(truck_weights.pop(0))
			else:
				bridge.append(0)
	return total_time

bridge_length, weight = 2, 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights)) # 8
bridge_length, weight = 100, 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights)) # 101
bridge_length, weight = 100, 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights)) # 110