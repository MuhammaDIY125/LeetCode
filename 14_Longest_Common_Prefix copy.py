class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ""
        n = -1
        for i in min(strs, key=len):
            lampocha = True
            n += 1
            for j in strs[1:]:
                if j[n] != i:
                    lampocha = False
                    break
            if lampocha:
                s = s + i
            else:
                break
        return s
    
s1 = Solution()
strs = ["flower","flow","flight"]
print(s1.longestCommonPrefix(strs))