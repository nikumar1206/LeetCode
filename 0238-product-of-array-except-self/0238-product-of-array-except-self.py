class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result_arr[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result_arr[i] *= postfix
            postfix *= nums[i]
        return result_arr