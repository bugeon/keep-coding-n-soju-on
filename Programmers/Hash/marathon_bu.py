def solution(participant, completion):
	participant = sorted(participant)
	completion = sorted(completion)
	
	for i in range(len(completion)):
		if participant[i] != completion[i]:
			return participant[i]
	return participant[len(participant) - 1]


# participant, completion = ["leo", "kiki", "eden"],	["eden", "kiki"]
# "leo"
# participant, completion = ["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"]
# "vinko"
# participant, completion = ["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]
# "mislav"

# print(solution(participant, completion))
