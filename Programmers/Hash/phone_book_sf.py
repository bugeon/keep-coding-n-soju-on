def solution(phone_book):
	answer = True

	num = 0
	table = dict()
	for pn in phone_book:
		table[pn] = 1
	i = 1
	while answer and i < 21:
		for pn in phone_book:
			nn = pn[:i]
			if nn in table and nn != pn:
				answer = False
		i += 1

	return answer


```
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (2.68ms, 10.4MB)
테스트 15 〉	통과 (2.51ms, 10.3MB)
테스트 16 〉	통과 (4.49ms, 10.4MB)
테스트 17 〉	통과 (5.29ms, 10.3MB)
테스트 18 〉	통과 (6.18ms, 10.3MB)
테스트 19 〉	통과 (6.74ms, 10.6MB)
테스트 20 〉	통과 (8.34ms, 10.6MB)
효율성  테스트
테스트 1 〉	통과 (2.21ms, 11.3MB)
테스트 2 〉	통과 (2.26ms, 11.3MB)
테스트 3 〉	통과 (474.13ms, 46.8MB)
테스트 4 〉	통과 (561.82ms, 34.8MB)
```
