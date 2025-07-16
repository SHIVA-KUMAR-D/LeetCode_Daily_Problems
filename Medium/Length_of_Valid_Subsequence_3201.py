from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        def alternate(start_parity):
            count = 0
            expected = start_parity
            for num in nums:
                if num % 2 == expected:
                    count += 1
                    expected ^= 1
            return count

        count_even = sum(1 for x in nums if x % 2 == 0)
        count_odd = len(nums) - count_even

        return max(alternate(0), alternate(1), count_even, count_odd)
# Example usage
print(Solution().maximumLength([1, 2, 3, 4, 5]))

