class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

s1 = Solution()
nums = [0,2,1,5,3,4]
print(s1.buildArray(nums))