class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_indices = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in hash_indices:
                return [i, hash_indices[diff]]
            else:
                hash_indices[num] = i
        