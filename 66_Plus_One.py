class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in (str(int(''.join([str(i) for i in digits])) + 1))]

s1 = Solution()
digits = [1,2,3]
print(s1.plusOne(digits))