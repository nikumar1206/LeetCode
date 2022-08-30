class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      windowLeft = 0
      _sum = 0
      min_len = inf
      for windowRight, num in enumerate(nums):
        _sum += num
        while _sum >= target:
          min_len = min(min_len, (windowRight-windowLeft + 1))
          _sum -= nums[windowLeft]
          windowLeft += 1
      if min_len == inf:
        return 0
      else:
        return min_len