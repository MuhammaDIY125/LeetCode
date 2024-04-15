class Solution:
    def mySqrt(self, x: int) -> int:
        natija = 0
        while True:
            if natija ** 2 > x:
                return natija - 1
            natija += 1
        # return int(x ** 0.5)

s1 = Solution()
x = 8
print(s1.mySqrt(x))