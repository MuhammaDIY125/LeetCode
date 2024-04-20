class Solution:
    def shuffle(self, nums:list[int], n:int) -> list[int]:
        lst = []
        for i in range(n):
            lst.append(nums[i])
            lst.append(nums[i+n])
        return lst

s1 = Solution()
nums = [1,2,3,4,4,3,2,1]
n = 4
print(s1.shuffle(nums, n))