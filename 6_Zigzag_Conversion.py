# Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a, b = 0, numRows * 2 - 2
        while a <= b:
            c = a
            while c < len(s):
                print(s[a], end="")
                for i in range(b-a):
                    print(" ", end="")
                c += numRows














s1 = Solution()
s = "PAYPALISHIRING" # 1 <= s.length <= 1000
numRows = 4 # 1 <= numRows <= 1000
print(s1.convert(s, numRows))