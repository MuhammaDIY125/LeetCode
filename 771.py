class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            count += stones.count(i)
        return count

s1 = Solution()
jewels = "aA"
stones = "aAAbbbb"
print(s1.numJewelsInStones(jewels, stones))