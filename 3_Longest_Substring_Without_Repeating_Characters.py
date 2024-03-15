# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         s = str(s)
#         lst = []
#         st = ""
#         for i in s:
#             if i not in st:
#                 st += i
#             else:
#                 lst.append(st)
#                 st = i
#         lst.append(st)
#         maximum = max(lst, key=lambda x: len(x))
#         return len(maximum)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = str(s)
        lst = []
        st = ""
        for i in s:
            if i not in st:
                st += i
            else:
                lst.append(st)
                st = i
        lst.append(st)
        maximum = max(lst, key=lambda x: len(x))
        return len(maximum)

s1 = Solution().lengthOfLongestSubstring("abcabcbb")
print(s1)