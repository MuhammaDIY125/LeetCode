class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

s1 = Solution()
a = "11"
b = "1"
print(s1.addBinary(a, b))