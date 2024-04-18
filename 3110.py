class Solution:
    def scoreOfString(self, s: str) -> int:
        natija = 0
        for i in range(len(s)-1):
            natija += ((ord(s[i]) - ord(s[i+1]))**2)**0.5
        return int(natija)

s1 = Solution()
n = "hello"
print(s1.scoreOfString(n))