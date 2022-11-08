from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      nums_counter = Counter(nums)
      frequency_list = sorted(list(nums_counter.values()))[::-1]

      result_arr = []
      for i in range(k):
        for num in nums_counter:
          if nums_counter[num] == frequency_list[i]:
            del nums_counter[num]
            result_arr.append(num)
            break
      return result_arr