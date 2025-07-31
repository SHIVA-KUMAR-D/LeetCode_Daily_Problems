class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        prev = set()

        for num in arr:
            curr = {num}
            for p in prev:
                curr.add(p | num)
            prev = curr
            res.update(curr)

        return len(res)