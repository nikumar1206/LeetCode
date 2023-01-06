from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_arr = []
        count_nums = Counter(nums)
        sort_val = set(sorted(count_nums.values())[::-1][:k])
        for key in count_nums:
            if count_nums[key] in sort_val:
                f_arr.append(key)
        return f_arr