class Solution:
    def longestPalindrome(self, s: str) -> str:
        lst = [s[0]]
        while len(s) > 1:
            for i in range(len(s), 1, -1):
                j = s[:i]
                if j == j[::-1]:
                    lst.append(j)
            s = s[1:]
        return max(lst, key=lambda x: len(x))

s = input(">>> ")
print(Solution().longestPalindrome(s))