# # Zigzag Conversion
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         lst = [[]] * numRows
#         n = numRows


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 2:
            toq = ""
            juft = ""
            for i in range(len(s)):
                if i % 2:
                    toq += s[i]
                else:
                    juft += s[i]
            return juft + toq
        if numRows == 1:
            return s
        box = "_" * len(s) + " "
        n = numRows * 2 - 2
        natija = s[0]
        s = "_" + s[1:] + " "
        
        if len(s) - 1 > numRows:
            for i in range(1, len(s) // n + 1):
                natija += s[i*n]
                s = s[:i*n] + "_" + s[i*n+1:]
        while s != box:
            for i in range(len(s) - 1):
                if s[i] != "_" and (s[i-1] == "_" or s[i+1]== "_"):
                    natija += s[i]
                    s = s[:i] + "*" + s[i+1:]
            s = s.replace("*", "_")
        return natija
    



s1 = Solution()
s = "PAHNAPLSIIGYIR" # 1 <= s.length <= 1000
numRows = 4 # 1 <= numRows <= 1000
print(s1.convert(s, numRows))

# PLIAPSYRHAIGNI
# PINALSIGYAHRPI