class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

s1 = Solution()
address = "1.1.1.1"
print(s1.defangIPaddr(address))