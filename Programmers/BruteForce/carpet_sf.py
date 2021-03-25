def solution(brown, yellow):
	answer = list()
	for i in range(3, brown-2):
		find = False
		for j in range(3, brown-2):
			if i < j:
				break
			if ((2 * i) + (2 * j)) - 4 == brown and (i-2)*(j-2) == yellow:
				answer = [i, j]
				find = True
				break
		if find:
			break
	
	return answer

'''
제곱근을 이용해 둘레 확인 -> 속도차 발생
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]
'''
