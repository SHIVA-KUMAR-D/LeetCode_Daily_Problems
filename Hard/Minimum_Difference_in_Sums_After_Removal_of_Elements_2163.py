from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n

        # 1. Left part: Max heap to store the smallest n elements (simulate max heap using negation)
        left_heap = []
        left_sum = 0
        left_sums = [0] * total_len

        for i in range(total_len):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                removed = -heapq.heappop(left_heap)
                left_sum -= removed
            if len(left_heap) == n:
                left_sums[i] = left_sum

        # 2. Right part: Min heap to store the largest n elements
        right_heap = []
        right_sum = 0
        right_sums = [0] * total_len

        for i in range(total_len - 1, -1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                removed = heapq.heappop(right_heap)
                right_sum -= removed
            if len(right_heap) == n:
                right_sums[i] = right_sum

        # 3. Calculate minimum difference
        result = float('inf')
        for i in range(n - 1, 2 * n):
            result = min(result, left_sums[i] - right_sums[i + 1])

        return result
