class Solution:
    def maxSum(self, nums: List[int]) -> int:
        allneg = True
        for num in nums:
            if num>=0:
                allneg = False
                break
        if allneg:
            return max(nums)
        lst = set(num for num in nums if num>=0)
        return sum(lst)