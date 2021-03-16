def solution(clothes):
	answer = 1
	hash_clothes = {}
	for item, category in clothes:
		if not category in hash_clothes:
			hash_clothes[category] = 2
		else:
			hash_clothes[category] += 1
	
	for category in hash_clothes.keys():
		answer *= hash_clothes[category]
	return answer - 1

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) # 5
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes)) # 3