def solution(answers):
    answer = []
    n = len(answers)
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0]
    
    for i in range(n):
      if answers[i] == student1[i % 5]:
        correct[0] += 1
      if answers[i] == student2[i % 8]:
        correct[1] += 1
      if answers[i] == student3[i % 10]:
        correct[2] += 1
    
    max_count = max(correct)
    for i, count in enumerate(correct):
      if max_count == count:
        answer.append(i + 1)
    return answer