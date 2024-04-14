# Zigzag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = []
        for i in range(numRows):
            lst.append([])
        n = 0
        lampochka = True
        for i in s:
            print(n, i)
            lst[n].append(i)
            if n < numRows - 1 and lampochka:
                n += 1
            elif n == numRows - 1:
                n -= 1
                lampochka = False
            elif n > 0 and not lampochka:
                n -= 1
            else:
                n += 1
                lampochka = True
        natija = ''
        for i in lst:
            natija += ''.join(i)
        return natija
        print(natija)


s1 = Solution()
s = "PAYPALISHIRING"
numRows = 4
s1.convert(s, numRows)

# PLIAPSYRHAIGNI
# PINALSIGYAHRPI