class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_ptr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[i]
        return unique_ptr + 1, nums


s1 = Solution()
s = [0,0,1,1,1,2,2,3,3,4]
print(s1.removeDuplicates(s))