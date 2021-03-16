def solution(prices):
	answer = list()
	length = len(prices)
	for i in range(length):
		j = 0
		while j + i + 1 < length:
			j += 1
			if prices[i] > prices[j + i]:
				break
		answer.append(j)

	return answer

```
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (1.11ms, 10.3MB)
테스트 4 〉	통과 (1.17ms, 10.3MB)
테스트 5 〉	통과 (1.56ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.39ms, 10.3MB)
테스트 8 〉	통과 (0.82ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (1.66ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (166.02ms, 18.9MB)
테스트 2 〉	통과 (129.87ms, 17.5MB)
테스트 3 〉	통과 (212.94ms, 19.6MB)
테스트 4 〉	통과 (149.70ms, 18.3MB)
테스트 5 〉	통과 (99.20ms, 17.1MB)
채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
```
