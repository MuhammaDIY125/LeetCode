class Solution:
    def isValid(self, s: str) -> bool:
        ttt = {'(':')', '[': ']', '{':'}'}
        lst = []
        for i in s:
            if not(i in ttt and lst):
                return False
            elif i not in ttt:
                if i == lst[-1]:
                    lst.pop()
                else:
                    return False
            else:
                lst.append(ttt[i])
        if lst:
            return False
        return True
    
s1 = Solution()
s = '()[]{}'
print(s1.isValid(s))