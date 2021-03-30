# diijkstra
import heapq


def solution(n, costs):
	graph = {str(node): list() for node in range(n)}
	for c in costs:
		graph[str(c[0])].append((str(c[1]), c[2]))
		graph[str(c[1])].append((str(c[0]), c[2]))
	answer = float('inf')
	for i in range(n):
		distances = {str(node): float('inf') for node in range(n)}
		distances_answer = {str(node): 0 for node in range(n)}
		distances[str(i)] = 0
		queue = list()
		heapq.heappush(queue, [str(i), distances[str(i)]])
		
		while queue:
			c_dest, c_dist = heapq.heappop(queue)
			for new_node in graph[c_dest]:
				n_dest = new_node[0]
				n_dist = new_node[1]
				dist = c_dist + n_dist
				if dist < distances[n_dest]:
					distances[n_dest] = dist
					distances_answer[n_dest] = n_dist
					heapq.heappush(queue, [n_dest, dist])
		if answer > sum(distances_answer.values()):
			answer = sum(distances_answer.values())

	return answer


'''
도와줘!!! 3,4,5,6 틀림.....하.......
'''
