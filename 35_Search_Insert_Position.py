class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if max(nums) < target:
            return len(nums)
        if min(nums) > target:
            return 0
        for i, v in enumerate(nums[1:-1]):
            if v > target:
                return i

s1 = Solution()
nums = [1,3,5,6]
target = 5
print(s1.searchInsert(nums, target))