class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    answer = []
    nums_with_count = {}
    for n in nums:
      if n in nums_with_count.keys():
        nums_with_count[n] += 1
      else:
        nums_with_count[n] = 1
    
    nums_with_count = sorted(nums_with_count.items(), key = lambda x : x[1], reverse = True)

    for i in range(k):
      answer.append(nums_with_count[i][0])
    return answer