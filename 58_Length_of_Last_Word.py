class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        return len(s.rsplit(maxsplit=1)[-1])

s1 = Solution()
s = "   Hello    World  "   
print(s1.lengthOfLastWord(s))