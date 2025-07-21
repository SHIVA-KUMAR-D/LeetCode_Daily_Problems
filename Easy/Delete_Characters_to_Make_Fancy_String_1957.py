class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 1  # count of consecutive same characters

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  # reset count for new character

            if count < 3:
                result.append(s[i])

        # always add the first character
        return s[0] + ''.join(result)
