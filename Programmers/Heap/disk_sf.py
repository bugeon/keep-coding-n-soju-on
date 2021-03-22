import heapq


def solution(jobs):
	new_jobs = list()
	real_job = list()
	for j in jobs:
		heapq.heappush(new_jobs, (j[0], j[1]))
	
	current_time = 0
	answer = 0
	pop_length = 0

	for rj in filter(lambda x: x[0] <= current_time, new_jobs):
		heapq.heappush(real_job, (rj[1], rj[0]))
		pop_length += 1
	for i in range(pop_length):
		heapq.heappop(new_jobs)

	while len(real_job) > 0 or len(new_jobs):
		# filter 0th < current time, then push real job
		# pop real job add current time += 1th
		# answer +=  current_time
		
		if len(real_job) > 0:
			current_job = heapq.heappop(real_job)
			current_time += current_job[0]
			answer += (current_time - current_job[1])
		else:
			current_time = new_jobs[0][0]

		pop_length = 0
		for rj in filter(lambda x: x[0] <= current_time, new_jobs):
			heapq.heappush(real_job, (rj[1], rj[0]))
			pop_length += 1
		for i in range(pop_length):
			heapq.heappop(new_jobs)
	
	return answer//len(jobs)
