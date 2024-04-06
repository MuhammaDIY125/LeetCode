class Solution:
    def reverse(self, x: int) -> int:
        z = 1
        if x < 0:
            z = -1
            x *= -1
        x = int(str(x)[::-1])
        if x > 2147483412:
            return 0
        return x * z


s1 = Solution()
print(s1.reverse(123456789))