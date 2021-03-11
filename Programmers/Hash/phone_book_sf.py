def solution(phone_book):
	answer = True

	num = 0
	min_len = 21
	table = dict()
	for pn in phone_book:
		table[pn] = 1
		if min_len > len(pn):
			min_len = len(pn)

	i = min_len
	while answer and i < 21:
		for pn in phone_book:
			nn = pn[:i]
			if nn in table and nn != pn:
				answer = False
		i += 1

	return answer


```
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (2.26ms, 10.3MB)
테스트 15 〉	통과 (2.09ms, 10.4MB)
테스트 16 〉	통과 (3.07ms, 10.4MB)
테스트 17 〉	통과 (0.98ms, 10.3MB)
테스트 18 〉	통과 (3.25ms, 10.4MB)
테스트 19 〉	통과 (1.43ms, 10.5MB)
테스트 20 〉	통과 (4.15ms, 10.6MB)
효율성  테스트
테스트 1 〉	통과 (2.54ms, 11.3MB)
테스트 2 〉	통과 (2.75ms, 11.4MB)
테스트 3 〉	통과 (77.12ms, 46.8MB)
테스트 4 〉	통과 (68.24ms, 34.6MB)
채점 결과
정확성: 83.3
효율성: 16.7
합계: 100.0 / 100.0
```
