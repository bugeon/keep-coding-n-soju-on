def solution(genres, plays):
	table_count = dict()
	table_list = dict()
	for i in range(len(genres)):
		h = hash(genres[i])
		if h in table_count:
			table_count[h] += plays[i]
			table_list[h].append((i, plays[i]))
		else:
			table_count[h] = plays[i]
			table_list[h] = [(i, plays[i])]

	answer = []

	for h in sorted(table_count.items(), key=lambda item: item[1], reverse=True):
		table_list[h] = sorted(table_list[h[0]], key=lambda item: item[1], reverse=True)
		answer.append(table_list[h][0][0])
		if len(table_list[h]) > 1:
			answer.append(table_list[h][1][0])

	return answer

```
실행 결과
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.3MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.06ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.10ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (0.09ms, 10.3MB)
테스트 14 〉	통과 (0.10ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
```
