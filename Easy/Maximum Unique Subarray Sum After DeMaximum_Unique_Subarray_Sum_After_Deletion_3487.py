class Solution:
    def maxSum(self, nums) -> int:# Maximum Unique Subarray Sum After Deletion
        allneg = True
        for num in nums:
            if num>=0: # check if there is any non-negative number
                allneg = False
                break
        if allneg:# if all numbers are negative
            return max(nums)
        lst = set(num for num in nums if num>=0)
        return sum(lst)#this is the maximum unique subarray sum after deletion