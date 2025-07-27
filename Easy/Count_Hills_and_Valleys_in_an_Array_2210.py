# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

# Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

# Return the number of hills and valleys in nums.

class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        
        # Remove consecutive duplicates to simplify comparison
        simplified = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                simplified.append(nums[i])
        for i in range(1, len(simplified) - 1):
            if simplified[i] > simplified[i - 1] and simplified[i] > simplified[i + 1]:
                count += 1  
            elif simplified[i] < simplified[i - 1] and simplified[i] < simplified[i + 1]:
                count += 1 

        return count