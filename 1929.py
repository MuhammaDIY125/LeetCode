class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums

s1 = Solution()
n = [1, 2, 1]
print(s1.getConcatenation(n))