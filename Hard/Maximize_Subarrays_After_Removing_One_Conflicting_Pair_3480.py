class Solution:
    def maxSubarrays(self, n, conflictingPairs):
        lefts = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            a, b = min(a, b), max(a, b)
            lefts[b].append(a)

        ans = 0
        top1 = 0
        top2 = 0
        bonus = [0] * (n + 1)

        for b in range(1, n + 1):
            for a in lefts[b]:
                if a > top1:
                    top2 = top1
                    top1 = a
                elif a > top2:
                    top2 = a
            ans += b - top1
            if top1 > 0:
                bonus[top1] += top1 - top2

        return ans + max(bonus)
