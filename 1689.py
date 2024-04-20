class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(list(n)))

s1 = Solution()
n = "27346209830709182346"
print(s1.minPartitions(n))