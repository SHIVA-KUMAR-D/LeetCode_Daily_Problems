"""  A fancy string is a string where no three consecutive characters are equal.Given a string s, delete the minimum possible number of characters from s to make it fancy.Return the final string after the deletion. It can be shown that the answer will always be unique. """

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
