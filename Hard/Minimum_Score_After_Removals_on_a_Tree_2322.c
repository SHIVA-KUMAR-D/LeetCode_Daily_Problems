from collections import defaultdict

class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        xor = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        parent = [-1] * n
        time = [0]

        def dfs(u, par):
            xor[u] = nums[u]
            parent[u] = par
            time[0] += 1
            in_time[u] = time[0]
            for v in graph[u]:
                if v != par:
                    xor[u] ^= dfs(v, u)
            time[0] += 1
            out_time[u] = time[0]
            return xor[u]

        total_xor = dfs(0, -1)

        def is_descendant(u, v):  # is u in v's subtree
            return in_time[v] <= in_time[u] <= out_time[v]

        children = [i for i in range(n) if parent[i] != -1]
        min_score = float('inf')

        for i in range(len(children)):
            for j in range(i + 1, len(children)):
                a, b = children[i], children[j]

                if is_descendant(a, b):
                    x1 = xor[a]
                    x2 = xor[b] ^ xor[a]
                    x3 = total_xor ^ xor[b]
                elif is_descendant(b, a):
                    x1 = xor[b]
                    x2 = xor[a] ^ xor[b]
                    x3 = total_xor ^ xor[a]
                else:
                    x1 = xor[a]
                    x2 = xor[b]
                    x3 = total_xor ^ xor[a] ^ xor[b]

                min_score = min(min_score, max(x1, x2, x3) - min(x1, x2, x3))

        return min_score
