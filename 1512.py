class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

s1 = Solution()
nums = [1,1,1,1]
print(s1.numIdenticalPairs(nums))