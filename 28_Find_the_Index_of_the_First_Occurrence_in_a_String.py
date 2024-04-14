class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while haystack:
            if haystack.startswith(needle):
                return i
            i += 1
            haystack = haystack[1:]
        return -1

s1 = Solution()
haystack = "leetcode"
needle = "leeto"
print(s1.strStr(haystack, needle))