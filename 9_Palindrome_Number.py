class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False

s1 = Solution()
print(s1.isPalindrome(97))