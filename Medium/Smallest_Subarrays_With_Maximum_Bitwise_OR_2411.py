class Solution(object):
    def smallestSubarrays(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    n = len(nums)
    answer = [1] * n
    last_seen = [-1] * 32  # For each bit position (0 to 31)
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Update the last seen index for all set bits
        for b in range(32):
            if nums[i] & (1 << b):
                last_seen[b] = i
        
        # Find farthest index we need to reach to cover all bits
        max_reach = i
        for b in range(32):
            if last_seen[b] != -1:
                max_reach = max(max_reach, last_seen[b])
        
        answer[i] = max_reach - i + 1
    
    return answer