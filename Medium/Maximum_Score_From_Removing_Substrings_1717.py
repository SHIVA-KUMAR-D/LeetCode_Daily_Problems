class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pattern(s: str, first: str, second: str, score: int) -> (str, int):
            stack = []
            total = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(ch)
            return "".join(stack), total

        # Step 1: prioritize the pattern with higher score
        if x > y:
            s, score1 = remove_pattern(s, 'a', 'b', x)
            s, score2 = remove_pattern(s, 'b', 'a', y)
        else:
            s, score1 = remove_pattern(s, 'b', 'a', y)
            s, score2 = remove_pattern(s, 'a', 'b', x)

        return score1 + score2
